from handlers.risk_score_processor import INELEGIBLE
from handlers.risk_score_processor.base import RiskProcessor


class DisabilityRisk(RiskProcessor):

    def __init__(self, kwargs):
        super().__init__(kwargs)
        self.disability_score = sum(kwargs["risk_questions"])

    def calculate(self) -> int:

        self.disability_score = self.age_deduct(self.disability_score)
        self.disability_score = self.income_deduct(self.disability_score)
        self.disability_score = self.mortgage_increase(self.disability_score)
        self.disability_score = self.dependents_increase(self.disability_score)
        self.disability_score = self.married_deduct(self.disability_score)

        return self.disability_score

    def evaluate(self) -> str:

        if not self.income or self.age > 60:
            return INELEGIBLE

        self.calculate()
        return self.response_result(self.disability_score)

