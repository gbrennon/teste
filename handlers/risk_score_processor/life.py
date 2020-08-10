from handlers.risk_score_processor import INELEGIBLE
from handlers.risk_score_processor.base import RiskProcessor


class LifeRisk(RiskProcessor):

    def __init__(self, kwargs):
        super().__init__(kwargs)
        self.life_score = sum(kwargs["risk_questions"])

    def calculate(self) -> int:

        self.life_score = self.age_deduct(self.life_score)
        self.life_score = self.income_deduct(self.life_score)
        self.life_score = self.dependents_increase(self.life_score)
        self.life_score = self.married_increase(self.life_score)

        return self.life_score

    def evaluate(self) -> str:

        if self.age > 60:
            return INELEGIBLE

        self.calculate()
        return self.response_result(self.life_score)

