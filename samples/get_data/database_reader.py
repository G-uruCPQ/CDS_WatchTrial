"""
Gadgetbridge SQLite Database Reader
===================================

GadgetbridgeからエクスポートされたSQLiteデータベースを
読み取り、測定データをPythonの辞書形式で取得する。

Usage:
  from database_reader import GadgetbridgeDB

  db = GadgetbridgeDB("Gadgetbridge.db")

  # 最新の測定値
  latest = db.get_latest()
  print(latest["heart_rate"])

  # 日次集計
  daily = db.get_daily()
  if daily is not None:
    print(daily["steps"])

Features:
  - SQLiteへの読み取り専用接続
  - 測定項目の一括取得
  - 欠測値の処理
  - 記録日時・経過時間の付加

Notes:
  本ライブラリはエクスポート済みDBを参照する。
  Smart Bandとの同期やDBエクスポートは行わない。
"""

import sqlite3
import time
from pathlib import Path
from contextlib import closing
from datetime import datetime, timezone, timedelta


JST = timezone(timedelta(hours=9))


class GadgetbridgeDB:
  def __init__(self, db_path: str, device_id: int = 1):
    self.db_path = Path(db_path).expanduser().resolve()
    self.device_id = device_id

  # ===== SQLite共通処理 =====

  def _connect(self) -> sqlite3.Connection:
    uri = self.db_path.as_uri() + "?mode=ro"
    conn = sqlite3.connect(uri, uri=True)
    conn.row_factory = sqlite3.Row
    return conn

  def _fetch_one(self, conn: sqlite3.Connection, sql: str, params: tuple = ()) -> dict | None:
    """Execute a parameterized SELECT and return a dict, or None."""
    row = conn.execute(sql, params).fetchone()
    return dict(row) if row else None

  # ===== 睡眠セッション取得 =====
  def _get_sleep_sessions(self, day: str) -> list[dict]:
    """
    指定したJSTの起床日に属する睡眠セッションを取得する。

    Args:
      day (str): 起床日（YYYY-MM-DD）

    Returns:
      list[dict]: 睡眠セッションのリスト。
                  データが無い場合は空リスト。
                  時刻はUnix秒、時間は分
    """
    start = datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=JST)
    end = start + timedelta(days=1)

    sql = """
      SELECT *
      FROM XIAOMI_SLEEP_TIME_SAMPLE
      WHERE DEVICE_ID = ?
        AND WAKEUP_TIME >= ?
        AND WAKEUP_TIME < ?
      ORDER BY WAKEUP_TIME
    """

    params = (self.device_id, int(start.timestamp() * 1000), int(end.timestamp() * 1000))

    with closing(self._connect()) as conn:
      rows = conn.execute(sql, params).fetchall()

    return[
      {
        "sleep_start": row["TIMESTAMP"] // 1000,
        "wakeup_time": row["WAKEUP_TIME"] // 1000 if row["WAKEUP_TIME"] is not None else None,
        "total_duration": row["TOTAL_DURATION"],
        "deep_sleep_duration": row["DEEP_SLEEP_DURATION"],
        "light_sleep_duration": row["LIGHT_SLEEP_DURATION"],
        "rem_sleep_duration": row["REM_SLEEP_DURATION"],
        "awake_duration": row["AWAKE_DURATION"]
      }
      for row in rows
    ]

  # ===== 最新の測定データ =====

  def get_latest(self) -> dict | None:
    """
    Gadgetbridgeに保存された各測定項目の最新値を取得する。

    測定項目ごとに最新の有効なレコードを検索する。
    各項目の測定時刻は必ずしも一致しない。

    Returns:
      dict:
        {
          "steps": int | None,
          "heart_rate": int | None,
          "stress": int | None,
          "spo2": int | None,
          "battery_level": int | None,
          "measured_at": {
            "<key>": int | None
          },
          "age_seconds": {
            "<key>": int | None
          }
        }

        Keys:
          steps:
            最新1分間の歩数 [steps]。
            0步も有効な測定値として扱う。
          heart_rate:
            最新の有効な心拍数 [bpm]。
          stress:
            最新のストレス値（無次元）。
          spo2:
            最新の血中酸素飽和度 [%]。
          battery_level:
            最新のバッテリー残量 [%]。
          measured_at:
            各項目の記録日次。
            Unixタイムスタンプ（秒）。
          age_seconds:
            現在時刻から各項目の記録日時までの経過時間 [s]。

      Notes:
        - 測定値が存在しない場合はNoneを返す。
        - 0が欠測を意味する項目では無効値を除外する。
        - データはGadgetbridgeの最終同期時点のもの。
        - age_secondsは測定値の鮮度確認に利用する。
        - 各項目の欠測値判定は暫定仕様を含む。
    """

    fields = ("steps", "heart_rate", "stress", "spo2", "battery_level")

    data = {key: None for key in fields}
    data["measured_at"] = {key: None for key in fields}
    data["age_seconds"] = {key: None for key in fields}

    now = int(time.time())

    def store(key, row):
      if row is None:
        return

      timestamp = int(row["TIMESTAMP"])
      data[key] = row["value"]
      data["measured_at"][key] = timestamp
      data["age_seconds"][key] = now - timestamp

    with closing(self._connect()) as conn:

      # 歩数：0步も有効
      row = self._fetch_one(conn, """
        -- 歩数
        SELECT TIMESTAMP, STEPS AS value
        FROM XIAOMI_ACTIVITY_SAMPLE
        WHERE DEVICE_ID = ?
        ORDER BY TIMESTAMP DESC
        LIMIT 1;
      """, (self.device_id,))
      store("steps", row)

      # 測定値ごとの有効データ検索
      # カラム名と条件は内部定義の固定値のみ使用
      metrics = {
        "heart_rate": ("HEART_RATE", "HEART_RATE BETWEEN 1 AND 254"),
        "stress"    : ("STRESS", "STRESS > 0"),
        "spo2"      : ("SPO2", "SPO2 BETWEEN 1 AND 100")
      }

      for key, (column, condition) in metrics.items():
        sql = f"""
          -- 心拍数・ストレス・SpO₂
          SELECT TIMESTAMP, {column} AS value
          FROM XIAOMI_ACTIVITY_SAMPLE
          WHERE DEVICE_ID = ?
            AND {condition}
          ORDER BY TIMESTAMP DESC
          LIMIT 1;
        """
        row = self._fetch_one(conn, sql, (self.device_id,))
        store(key, row)

      # バッテリー残量
      row = self._fetch_one(conn, """
        -- バッテリー残量
        SELECT TIMESTAMP, LEVEL AS value
        FROM BATTERY_LEVEL
        WHERE DEVICE_ID = ?
          AND BATTERY_INDEX = 0
        ORDER BY TIMESTAMP DESC
        LIMIT 1;
      """, (self.device_id,))
      store("battery_level", row)

    return data

  # ===== 日次集計データ =====

  def get_daily(self, day: str | None = None) -> dict | None:
    """
    指定日の活動・生体情報の日次集計を取得する。

    Args:
      day (str | None):
        取得対象の日付（"YYYY-MM-DD"形式）。
        Noneの場合はDB内の最新日を対象とする。

    Returns:
      dict | None:
        以下の構造の辞書を返す。
        対象日のデータがない場合はNone。<br>
        {
          "date": str,
          "steps": int | None,
          "calories": int | None,
          "heart_rate_resting": int | None,
          "heart_rate_avg": int | None,
          "heart_rate_min": int | None,
          "heart_rate_max": int | None,
          "stress_avg": int | None,
          "spo2_avg": int | None
          "sleep": {
            "total_duration": int | None
            "sessions": [
              {
                "sleep_start": int,
                "wakeup_time": int | None,
                "total_duration": int | None,
                "deep_sleep_duration": int | None,
                "light_sleep_duration": int | None,
                "rem_sleep_duration": int | None,
                "awake_duration": int | None
              }
            ]
          }
        }

        Keys:
          date:
            集計対象の日付（JST、YYYY-MM-DD）。
          steps:
            1日の合計歩数 [steps]。
          calories:
            1日の消費カロリー [kcal]。
          heart_rate_resting:
            安静時心拍数 [bpm]。
          heart_rate_avg:
            平均心拍数 [bpm]。
          heart_rate_min:
            最低心拍数 [bpm]。
          heart_rate_max:
            最高心拍数 [bpm]。
          stress_avg:
            平均ストレス値（無次元）。
          spo2_avg:
            平均血中酸素飽和度 [%]。
          sleep:
            睡眠セクション。

    Notes:
      - 日次集計はGadgetbridgeに保存された値を使用する。
      - 未測定を表す値は原則としてNoneに変換する。
      - 当日分は集計途中の可能性がある。
      - None指定時は今日ではなくDB内の最新日を返す。
      - 無効値の判定条件は解析結果に応じて更新する。
      - 睡眠データは起床日を基準に集計する。
      - 同日に複数の睡眠セッションがある場合、sessionsに全件格納する。
      - total_durationは各セッションの睡眠時間の合計。
      - 睡眠記録がない日はtotal_duration=None、sessions=[]とする。
      - 日次集計レコードが存在しない日は、睡眠記録があってもget_daily()はNoneを返す。
    """
  
    sql = """
      SELECT *
      FROM XIAOMI_DAILY_SUMMARY_SAMPLE
      WHERE DEVICE_ID = ?
    """

    params = [self.device_id]

    if day is not None:
      sql += """
        AND date(
          TIMESTAMP / 1000,
          'unixepoch', '+9 hours'
        ) = ?
      """
      params.append(day)

    sql += " ORDER BY TIMESTAMP DESC LIMIT 1"

    with closing(self._connect()) as conn:
      row = self._fetch_one(conn, sql, params)

    if row is None:
      return None

    # 0が未測定を示す項目を暫定的に除外
    def nonzero(value):
      return value if value is not None and value > 0 else None

    day_jst = datetime.fromtimestamp(row["TIMESTAMP"] / 1000, JST).date().isoformat()

    # 睡眠セッションの取得
    sessions = self._get_sleep_sessions(day_jst)
    durations = [s["total_duration"] for s in sessions if s["total_duration"] is not None]
    sleep = {
      "total_duration": sum(durations) if durations else None,
      "sessions": sessions
    }

    return {"date": day_jst, "steps": row["STEPS"], "calories": row["CALORIES"],
            "heart_rate_resting": nonzero(row["HR_RESTING"]), "heart_rate_avg": nonzero(row["HR_AVG"]),
            "heart_rate_min": nonzero(row["HR_MIN"]), "heart_rate_max": nonzero(row["HR_MAX"]),
            "stress_avg": nonzero(row["STRESS_AVG"]), "spo2_avg": nonzero(row["SPO2_AVG"]), "sleep": sleep}
