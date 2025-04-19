
from flask_dance.contrib.google import make_google_blueprint, google
from flask import Blueprint, jsonify
import jwt, time, os

SECRET_KEY = os.getenv("SECRET_KEY", "sentinelai_secret")

oauth_bp = Blueprint("oauth_bp", __name__)

google_bp = make_google_blueprint(
    client_id=os.getenv("OAUTH_GOOGLE_CLIENT_ID", "YOUR_GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("OAUTH_GOOGLE_CLIENT_SECRET", "YOUR_GOOGLE_SECRET"),
    redirect_to="google_callback"
)

@oauth_bp.route("/google_callback")
def google_callback():
    resp = google.get("/oauth2/v1/userinfo")
    if not resp.ok:
        return jsonify({"error": "OAuth failed"}), 400
    email = resp.json()["email"]
    payload = {
        "user": email,
        "provider": "google",
        "role": "viewer",
        "iat": int(time.time())
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token, "email": email})
