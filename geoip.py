
from flask import Blueprint, jsonify
from app.visual.geoip_mapper import map_ips_to_geo

geoip_api = Blueprint("geoip_api", __name__)

@geoip_api.route("/api/geoip")
def geoip():
    return jsonify(map_ips_to_geo())
