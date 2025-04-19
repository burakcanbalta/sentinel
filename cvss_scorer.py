def evaluate_cvss(log):
    base_score = 0.0
    vector = []

    reason = log.get("reason", "").lower()

    if "root" in log["user"].lower():
        base_score += 2.0
        vector.append("PR:N")
    if "ftp" in reason or "external" in log.get("ip_src", ""):
        base_score += 2.5
        vector.append("AV:N")
    if "command" in reason or "exec" in reason:
        base_score += 2.0
        vector.append("I:H")
    if "data" in reason or "download" in reason:
        base_score += 2.0
        vector.append("C:H")
    if "smb" in reason or "lateral" in reason:
        base_score += 1.0
        vector.append("S:U")

    base_score = min(round(base_score, 1), 10.0)
    severity = (
        "None" if base_score == 0 else
        "Low" if base_score < 4 else
        "Medium" if base_score < 7 else
        "High" if base_score < 9 else
        "Critical"
    )

    return {
        "score": base_score,
        "severity": severity,
        "vector": "/".join(vector)
    }
