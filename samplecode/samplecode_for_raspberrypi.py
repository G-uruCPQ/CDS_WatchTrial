import urllib.parse
import time
import requests

PHONE_URL = "http://{IPアドレス}:{ポート番号}"

# 日本語やスペースを含める場合はエンコードする
sender_name = urllib.parse.quote("ラズパイ監視システム")
message_body = urllib.parse.quote("居眠りを検知しました。起きろ。")
caller_name = urllib.parse.quote("さぼり検知マン")

# 通知を送る
requests.get(f"{PHONE_URL}/notify?sender={sender_name}&body={message_body}")

time.sleep(1)
#疑似電話（発信者名初期設定）
requests.get(f"{PHONE_URL}/start")

time.sleep(10)

requests.get(f"{PHONE_URL}/stop")

#疑似電話（発信者名変更）
requests.get(f"{PHONE_URL}/start?caller={caller_name}") 
