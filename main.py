
from flask import Flask
from flask_cors import CORS
from app.api.kpi import kpi_api
from app.api.plugin import plugin_api
from app.api.geoip import geoip_api
from app.swagger_config import configure_swagger

app = Flask(__name__)
CORS(app)

configure_swagger(app)

app.register_blueprint(kpi_api)
app.register_blueprint(plugin_api)
app.register_blueprint(geoip_api)

@app.route("/")
def home():
    return {"status": "SentinelAI API aktif."}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
