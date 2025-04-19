
from flask import Blueprint, jsonify
from app.analytics.kpi_panel import generate_kpis

kpi_api = Blueprint("kpi_api", __name__)

@kpi_api.route("/api/kpis")
def get_kpis():
    return jsonify(generate_kpis())
