
from flasgger import Swagger

def configure_swagger(app):
    Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "SentinelAI API",
            "description": "SentinelAI modüler siber güvenlik platformu API dokümantasyonu.",
            "version": "1.0"
        },
        "basePath": "/",
        "schemes": ["http"]
    })
