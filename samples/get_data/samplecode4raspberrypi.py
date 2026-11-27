import requests
import time
from datetime import datetime, timezone, timedelta

PHONE_URL = "http://{IPアドレス}:8081"

JST = timezone(timedelta(hours=9))

def format_time(timestamp):
  if timestamp is None:
    return "None"
  return datetime.fromtimestamp(timestamp, JST).strftime(
    "%Y-%m-%d %H:%M:%S"
  )

# データ更新
response = requests.get(f"{PHONE_URL}/data/export", timeout=10)
response.raise_for_status()
status = response.json()
print("export request:", status["export_request"])

time.sleep(2)

response = requests.get(f"{PHONE_URL}/data/status", timeout=10)
response.raise_for_status()
status = response.json()
modified, age = status["database_file_modified_at"], status["database_file_age_seconds"]
print(f"DB modified: {format_time(modified)} | Age: {age}s")

# 最新データ
response = requests.get(f"{PHONE_URL}/data/latest", timeout=10)
response.raise_for_status()

latest = response.json()
print(latest)


# 日次集計
response = requests.get(f"{PHONE_URL}/data/daily", timeout=10)
response.raise_for_status()

daily = response.json()
print(daily)


# 日付指定
response = requests.get(f"{PHONE_URL}/data/daily", params={"day": "2026-10-29"}, timeout=10)
response.raise_for_status()

daily = response.json()
print(daily)
