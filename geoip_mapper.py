import pandas as pd
import requests

def map_ips_to_geo(path="data/logs/anomaly_results.csv", limit=100):
    df = pd.read_csv(path).tail(limit)
    mapped = []

    for _, row in df.iterrows():
        ip = row["ip_src"]
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}").json()
            if r["status"] == "success":
                mapped.append({
                    "ip": ip,
                    "user": row["user"],
                    "score": row["anomaly_score"],
                    "time": row["timestamp"],
                    "lat": r["lat"],
                    "lon": r["lon"],
                    "country": r["country"]
                })
        except:
            continue

    return mapped
