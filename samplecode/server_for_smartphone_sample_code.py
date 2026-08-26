import subprocess
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
# ----------------------------------------------------
# 設定：最後のアクセスから何秒放置されたら終了するか (例: 300秒 = 5分)
IDLE_TIMEOUT_SEC = 60
# 最終アクセスの時刻を保持する変数（初期値は現在時刻）
last_access_time = time.time()
server_instance = None
# ----------------------------------------------------
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
      if path == "/start":
        caller_name = query.get("caller", ["Raspberry Pi"])[0]
        self.vibrate_start(caller_name)
        self.send_ok(f"Vibration STARTED (Caller: {caller_name})")
      elif path == "/stop":
        self.vibrate_stop()
        self.send_ok("Vibration STOPPED")
      elif path == "/vibrate":
        sec = float(query.get("sec", ["1"][0]))
        caller_name = query.get("caller", ["Raspberry Pi"])[0]
        self.vibrate_start(caller_name)
        time.sleep(sec)
        self.vibrate_stop()
        self.send_ok(f"Vibrated for {sec} seconds")
      elif path == "/notify":
        sender = query.get("sender", ["Wall Entity"])[0]
        body = query.get(
            "body", ["I am living in your walls. You may be concerned..."]
        )[0]
        self.send_notification(sender, body)
        self.send_ok(f"Notification sent from {sender}")
      else:
        self.send_response(404)
        self.end_headers()
    except Exception as e:
      print(f"Error handling request: {e}")
      self.send_response(500)
      self.end_headers()
      self.wfile.write(f"ERROR: {str(e)}\n".encode("utf-8"))
  def vibrate_start(self, caller_name="Raspberry Pi"):
    subprocess.run(
        [
            "am",
            "broadcast",
            "-a",
            "nodomain.freeyourgadget.gadgetbridge.command.DEBUG_INCOMING_CALL",
            "-e",
            "caller",
            caller_name,
            "-p",
            "nodomain.freeyourgadget.gadgetbridge",
        ],
  def vibrate_stop(self):
    subprocess.run(
        [
            "am",
            "broadcast",
            "-a",
            "nodomain.freeyourgadget.gadgetbridge.command.DEBUG_END_CALL",
            "-p",
            "nodomain.freeyourgadget.gadgetbridge",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
  def send_notification(self, sender, body):
    subprocess.run(
        [
            "am",
            "broadcast",
            "-a",
        	"nodomain.freeyourgadget.gadgetbridge.command.DEBUG_SEND_NOTIFICATION",
            "-e",
            "type",
            "GENERIC_SMS",
            "-e",
            "phoneNumber",
            "0123456789",
            "-e",
            "sender",
            sender,
            "-e",
            "subject",
            "Alert",
            "-e",
            "body",
            body,
            "-p",
            "nodomain.freeyourgadget.gadgetbridge",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
  def send_ok(self, msg):
    self.send_response(200)
    self.send_header("Content-type", "text/plain; charset=utf-8")
    self.end_headers()
    self.wfile.write(f"OK: {msg}\n".encode("utf-8"))

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
  server = HTTPServer(("0.0.0.0", 8080), RequestHandler)
  server_instance = server
  # アイドル監視スレッドをスタート
  watcher_thread = threading.Thread(target=idle_watcher, daemon=True)
  watcher_thread.start()
  print(
      f"Listening on 0.0.0.0:8080... (Auto-shutdown after {IDLE_TIMEOUT_SEC}s"
      " idle)"
  )
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print("\nManual shutdown...")
  finally:
    server.server_close()

