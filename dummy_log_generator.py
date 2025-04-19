import pandas as pd
import random
from datetime import datetime, timedelta

def generate_dummy_logs(filepath="data/logs/anomaly_results.csv", count=100):
    users = ["root", "admin", "guest", "hacker"]
    reasons = ["login", "command executed", "data exfiltration", "smb access", "ftp connection"]
    logs = []

    now = datetime.now()

    for i in range(count):
        log = {
            "timestamp": (now - timedelta(minutes=random.randint(1, 10000))).strftime("%Y-%m-%d %H:%M:%S"),
            "user": random.choice(users),
            "ip_src": f"192.168.1.{random.randint(1, 255)}",
            "anomaly_score": round(random.uniform(0.1, 0.99), 2),
            "reason": random.choice(reasons)
        }
        logs.append(log)

    df = pd.DataFrame(logs)
    df.to_csv(filepath, index=False)
    return f"{count} dummy logs generated at {filepath}"
