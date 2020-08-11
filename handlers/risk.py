import hashlib
import json

from flask import request, jsonify
from flask_restful import Resource
from handlers.risk_score_processor.auto import AutoRisk
from handlers.risk_score_processor.disability import DisabilityRisk
from handlers.risk_score_processor.home import HomeRisk
from handlers.risk_score_processor.life import LifeRisk
from schemas.schema import InputModel
from schemas.validator import validate_schema
from utils.redis_client import Cache
from utils.events import send_events


class RiskHandler(Resource):

    @staticmethod
    @validate_schema(InputModel)
    def post():
        data = request.json
        cache_client = Cache()

        hash_data = hashlib.sha1(json.dumps(data, sort_keys=True).encode()).hexdigest()

        cache_data = cache_client.get(name=hash_data)

        if cache_data:
            return jsonify(cache_data)

        response = {
            "auto": AutoRisk(data).evaluate(),
            "disability": DisabilityRisk(data).evaluate(),
            "home": HomeRisk(data).evaluate(),
            "life": LifeRisk(data).evaluate()
        }

        cache_client.set(name=hash_data, value=response, ex=5*60)

        send_events(response)

        return jsonify(response)
