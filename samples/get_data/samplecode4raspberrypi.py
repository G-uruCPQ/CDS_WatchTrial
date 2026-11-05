import requests

PHONE_URL = "http://{IPアドレス}:8081"

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
