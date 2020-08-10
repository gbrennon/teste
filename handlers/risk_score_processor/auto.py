from datetime import datetime
from handlers.risk_score_processor import INELEGIBLE
from handlers.risk_score_processor.base import RiskProcessor


class AutoRisk(RiskProcessor):

    def __init__(self, kwargs):
        super().__init__(kwargs)
        self.auto_score = sum(kwargs["risk_questions"])

    def vehicle_deduct(self, score: int) -> int:
        if self.vehicle_year >= datetime.now().year - 5:
            score += 1
        return score

    def calculate(self) -> int:

        self.auto_score = self.age_deduct(self.auto_score)
        self.auto_score = self.income_deduct(self.auto_score)
        self.auto_score = self.vehicle_deduct(self.auto_score)

        return self.auto_score

    def evaluate(self) -> str:

        if not self.vehicle_year:
            return INELEGIBLE

        self.calculate()
        return self.response_result(self.auto_score)




