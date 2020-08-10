from flask_restful import Api
from handlers.health_check import HealthCheckHandler
from handlers.risk import RiskHandler


def init_resources(app):
    api = Api()

    api.add_resource(HealthCheckHandler, "/risk/health-check")
    api.add_resource(RiskHandler, "/risk/v1")

    api.init_app(app)
