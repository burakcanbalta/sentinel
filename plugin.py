
from flask import Blueprint, jsonify
from app.plugins.run_plugin_engine import run_plugin

plugin_api = Blueprint("plugin_api", __name__)

@plugin_api.route("/api/plugin/<name>")
def run(name):
    return jsonify(run_plugin(name))
