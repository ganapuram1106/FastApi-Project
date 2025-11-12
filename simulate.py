import requests, random, time

BASE = "http://localhost:8000"

def create_robot(robot_id="RBT001", location="Site A"):
    url = f"{BASE}/robots"
    payload = {"robot_id": robot_id, "location": location}
    r = requests.post(url, json=payload)
    print("create_robot:", r.status_code, r.text)

def send_telemetry(robot_id="RBT001"):
    url = f"{BASE}/robots/{robot_id}/telemetry"
    payload = {
        "battery_level": round(random.uniform(5, 100), 2),
        "temperature": round(random.uniform(20, 90), 2)
    }
    r = requests.post(url, json=payload)
    print("send_telemetry:", r.status_code, r.text)

if __name__ == "__main__":
    create_robot()
    while True:
        send_telemetry()
        time.sleep(5)
