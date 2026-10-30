import threading
import traceback
import time
import json
import re
import sqlite3
from datetime import date
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import urllib.parse

from database_reader import GadgetbridgeDB

# ----------------------------------------------------
# 設定：最後のアクセスから何秒放置されたら終了するか (例: 300秒 = 5分)
IDLE_TIMEOUT_SEC = 1000
# 最終アクセスの時刻を保持する変数（初期値は現在時刻）
last_access_time = time.time()
server_instance = None
# ----------------------------------------------------

# ===== 設定 =====
HOST = "0.0.0.0"
PORT = 8081 # vibrationサーバー(8080)とは別ポート

DB_PATH = (
  Path(__file__).resolve().parent.parent
  / "Database" / "Gadgetbridge.db"
)

# DB解析はdatabase_reader.pyに任せる
reader = GadgetbridgeDB(str(DB_PATH), device_id=1)

# ===== HTTPリクエスト処理 =====
class RequestHandler(BaseHTTPRequestHandler):
  def address_string(self):
    return self.client_address[0]
  def do_GET(self):
    global last_access_time
    # リクエストが来たら最終アクセス時刻を現在に更新（タイマーリセット）
    last_access_time = time.time()
    parsed_path = urllib.parse.urlparse(self.path)
    path = parsed_path.path
    query = urllib.parse.parse_qs(parsed_path.query)
    try:
      # 最新の測定データ
      if path == "/data/latest":
        status_code = 200
        data = reader.get_latest()

      # 日次集計データ
      elif path == "/data/daily":
        status_code = 200
        day = None
        if "day" not in query:
          data = reader.get_daily()
        else:
          values = query["day"]
          if (len(values) == 1 and re.fullmatch(r"\d{4}-\d{2}-\d{2}", values[0])):
            day = values[0]
            try:
              date.fromisoformat(day)
            except ValueError:
              status_code = 400; data = {"error": "Invalid calendar date"}
            else:
              data = reader.get_daily(day=day)
          else:
            status_code = 400; data = {"error": "day must be YYYY-MM-DD"}

      # DBファイルの更新状況
      elif path == "/data/status":
        status_code = 200
        modified_at = int(DB_PATH.stat().st_mtime)
        data = {
          "database_file_modified_at": modified_at,
          "database_file_age_seconds": int(time.time()) - modified_at
        }

      # 未定義のエンドポイント
      else:
        status_code = 404
        data = {"error": "Endpoint not found"}

    except (OSError, sqlite3.Error):
      self.log_error("Database error:\n%s", traceback.format_exc())
      status_code = 500
      data = {"error": "Database access failed"}
    except Exception:
      self.log_error("Unexpected error:\n%s", traceback.format_exc())
      status_code = 500
      data = {"error": "Internal server error"}
    
    # HTTPレスポンス送信
    try:
      body = json.dumps(data, ensure_ascii=False).encode("utf-8")

      self.send_response(status_code)

      self.send_header("Content-Type", "application/json; charset=utf-8")
      self.send_header("Content-Length", str(len(body)))
      self.send_header("Cache-Control", "no-store")

      self.end_headers()
      self.wfile.write(body)
    except (BrokenPipeError, ConnectionResetError):
      self.log_message("Client disconnected")

# 一定時間アクセスがないかを監視するバックグラウンド関数
def idle_watcher():
  global last_access_time, server_instance
  while server_instance:
    time.sleep(10)  # 10秒ごとにチェック
    elapsed = time.time() - last_access_time
    if elapsed > IDLE_TIMEOUT_SEC:
      print(
        f"\n{IDLE_TIMEOUT_SEC}秒間アクセスがなかったため、サーバーを自動終了します。"
      )
      server_instance.shutdown()
      break


if __name__ == "__main__":
  server = HTTPServer((HOST, PORT), RequestHandler)
  server_instance = server
  # アイドル監視スレッドをスタート
  watch_thread = threading.Thread(target=idle_watcher, daemon=True)
  print(
    f"Listening on {HOST}:{PORT}... (Auto-shutdown after {IDLE_TIMEOUT_SEC}s"
    " idle)"
  )
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nManual shutdown...")
  finally:
    server.server_close()
