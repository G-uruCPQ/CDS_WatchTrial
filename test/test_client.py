import requests


SERVER = "http://127.0.0.1:8000"


def get_latest_steps():
    response = requests.get(
        f"{SERVER}/api/v1/latest/steps",
        timeout=1.0,
    )

    response.raise_for_status()

    result = response.json()

    return result["data"]["steps"]


if __name__ == "__main__":
    steps = get_latest_steps()

    print(f"steps = {steps}")