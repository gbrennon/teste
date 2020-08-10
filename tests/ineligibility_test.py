from handlers.risk_score_processor import INELEGIBLE
from handlers.risk_score_processor.auto import AutoRisk
from handlers.risk_score_processor.disability import DisabilityRisk
from handlers.risk_score_processor.home import HomeRisk
from handlers.risk_score_processor.life import LifeRisk
from tests import base_input


def test_auto_ineligible():
    input_data = base_input()
    input_data["vehicle"] = {}

    response = AutoRisk(input_data).evaluate()

    assert response == INELEGIBLE


def test_disability_ineligible():
    input_data = base_input()
    input_data["income"] = 0

    response = DisabilityRisk(input_data).evaluate()

    assert response == INELEGIBLE


def test_home_ineligible():
    input_data = base_input()
    input_data["house"] = {}

    response = HomeRisk(input_data).evaluate()

    assert response == INELEGIBLE


def test_disability_ineligible_2():
    input_data = base_input()
    input_data["age"] = 61

    response = DisabilityRisk(input_data).evaluate()

    assert response == INELEGIBLE


def test_lige_ineligible():
    input_data = base_input()
    input_data["age"] = 61

    response = LifeRisk(input_data).evaluate()

    assert response == INELEGIBLE

