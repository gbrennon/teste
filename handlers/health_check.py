from flask_restful import Resource


class HealthCheckHandler(Resource):

    @staticmethod
    def get():
        return "alive and kicking", 200
