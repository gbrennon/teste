from handlers.risk_score_processor import INELEGIBLE
from handlers.risk_score_processor.base import RiskProcessor


class HomeRisk(RiskProcessor):

    def __init__(self, kwargs):
        super().__init__(kwargs)
        self.home_score = sum(kwargs["risk_questions"])

    def calculate(self) -> int:

        self.home_score = self.age_deduct(self.home_score)
        self.home_score = self.income_deduct(self.home_score)
        self.home_score = self.mortgage_increase(self.home_score)

        return self.home_score

    def evaluate(self) -> str:
        if not self.house_ownership_status:
            return INELEGIBLE

        self.calculate()
        return self.response_result(self.home_score)
