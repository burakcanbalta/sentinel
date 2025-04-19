import pandas as pd
import zipfile
import os
from datetime import datetime

def archive_logs(log_file="data/logs/anomaly_results.csv", days_old=7):
    df = pd.read_csv(log_file)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    cutoff = pd.Timestamp.now() - pd.Timedelta(days=days_old)
    old_logs = df[df["timestamp"] < cutoff]

    if old_logs.empty:
        return {"status": "no logs to archive"}

    summary = {
        "log_count": len(old_logs),
        "max_score": old_logs["anomaly_score"].max(),
        "top_user": old_logs["user"].value_counts().idxmax(),
        "top_ip": old_logs["ip_src"].value_counts().idxmax()
    }

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_dir = f"data/archive/logs_{timestamp}"
    os.makedirs(archive_dir, exist_ok=True)

    old_logs.to_csv(f"{archive_dir}/archived.csv", index=False)

    with zipfile.ZipFile(f"{archive_dir}.zip", 'w') as zipf:
        zipf.write(f"{archive_dir}/archived.csv", arcname="archived.csv")

    os.remove(f"{archive_dir}/archived.csv")
    os.rmdir(archive_dir)

    return {"status": "archived", "zip": f"{archive_dir}.zip", "summary": summary}
