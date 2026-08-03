import time
import requests


SERVER = "http://127.0.0.1:8000"


def get_latest_steps():
    response = requests.get(
        f"{SERVER}/api/v1/latest/steps",
        timeout=0.5,
    )

    response.raise_for_status()

    return response.json()["data"]["steps"]


while True:
    try:
        steps = get_latest_steps()

        print(f"steps = {steps}")

    except requests.RequestException as e:
        print(f"API error: {e}")

    # 他の処理
    # update_sensor()
    # calculate_control()
    # send_motor_command()

    time.sleep(1)