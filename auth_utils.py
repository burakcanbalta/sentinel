
from functools import wraps
from flask import request, jsonify
import jwt, os

SECRET_KEY = os.getenv("SECRET_KEY", "sentinelai_secret")

def jwt_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[-1]
            if not token:
                return jsonify({"error": "Token eksik"}), 401
            try:
                decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                user_role = decoded.get("role", "viewer")
                if role and role != user_role:
                    return jsonify({"error": "Yetkisiz erişim"}), 403
                request.user = decoded
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token süresi dolmuş"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"error": "Geçersiz token"}), 401
            return f(*args, **kwargs)
        return wrapped
    return decorator
