from handlers.risk_score_processor import REGULAR
from handlers.risk_score_processor.disability import DisabilityRisk
from handlers.risk_score_processor.life import LifeRisk
from tests import base_input


def test_life_married():
    input_data = base_input()
    input_data["marital_status"] = "married"

    response = LifeRisk(input_data).evaluate()

    assert response == REGULAR


def test_disability_single():
    input_data = base_input()
    input_data["marital_status"] = "single"

    response = DisabilityRisk(input_data).evaluate()

    assert response == REGULAR
