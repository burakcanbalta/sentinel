import pandas as pd

def generate_kpis(path="data/logs/anomaly_results.csv"):
    df = pd.read_csv(path)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

    total = len(df)
    high = df[df["anomaly_score"] > 0.85].shape[0]
    low = df[df["anomaly_score"] <= 0.4].shape[0]
    top_user = df["user"].value_counts().idxmax()
    top_ip = df["ip_src"].value_counts().idxmax()
    by_day = df.groupby("date").size().reset_index(name="count").to_dict(orient="records")

    return {
        "total_events": total,
        "high_risk_count": high,
        "low_risk_count": low,
        "top_user": top_user,
        "top_ip": top_ip,
        "daily_distribution": by_day
    }
