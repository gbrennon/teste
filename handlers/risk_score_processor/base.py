from handlers.risk_score_processor import *


class RiskProcessor:

    def __init__(self, kwargs):
        self.age = kwargs["age"]
        self.dependents = kwargs["dependents"]
        self.house_ownership_status = kwargs["house"].get("ownership_status")
        self.income = kwargs["income"]
        self.marital_status = kwargs["marital_status"]
        self.vehicle_year = kwargs["vehicle"].get("year")

    def age_deduct(self, score: int) -> int:
        if self.age < 30:
            score -= 2
        if 30 <= self.age <= 40:
            score -= 1
        return score

    def income_deduct(self, score: int) -> int:
        if self.income > INCOME:
            score -= 1
        return score

    def mortgage_increase(self, score: int) -> int:
        if self.house_ownership_status == MORTGAGED:
            score += 1
        return score

    def dependents_increase(self, score: int) -> int:
        if self.dependents:
            score += 1
        return score

    def married_increase(self, score: int) -> int:
        if self.marital_status == MARRIED:
            score += 1
        return score

    def married_deduct(self, score: int) -> int:
        if self.marital_status == MARRIED:
            score -= 1
        return score

    @staticmethod
    def response_result(score: int) -> str:
        if score <= 0:
            return ECONOMIC
        if score == 1 or score == 2:
            return REGULAR
        if score >= 3:
            return RESPONSIBLE