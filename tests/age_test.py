from handlers.risk_score_processor.auto import AutoRisk
from handlers.risk_score_processor.disability import DisabilityRisk
from handlers.risk_score_processor.home import HomeRisk
from handlers.risk_score_processor.life import LifeRisk
from handlers.risk_score_processor import ECONOMIC, REGULAR
from tests import base_input


def test_auto_age_under_30():
    input_data = base_input()
    input_data["age"] = 29

    response = AutoRisk(input_data).evaluate()

    assert response == ECONOMIC


def test_disability_age_under_30():
    input_data = base_input()
    input_data["age"] = 29

    response = DisabilityRisk(input_data).evaluate()

    assert response == ECONOMIC


def test_home_age_under_30():
    input_data = base_input()
    input_data["age"] = 29

    response = HomeRisk(input_data).evaluate()

    assert response == ECONOMIC


def test_life_age_under_30():
    input_data = base_input()
    input_data["age"] = 29

    response = LifeRisk(input_data).evaluate()

    assert response == REGULAR


def test_auto_age_between_30_40():
    input_data = base_input()
    input_data["age"] = 30

    response = AutoRisk(input_data).evaluate()

    assert response == REGULAR


def test_disability_age_between_30_40():
    input_data = base_input()
    input_data["age"] = 30

    response = DisabilityRisk(input_data).evaluate()

    assert response == ECONOMIC


def test_home_age_between_30_40():
    input_data = base_input()
    input_data["age"] = 40

    response = HomeRisk(input_data).evaluate()

    assert response == ECONOMIC


def test_life_age_between_30_40():
    input_data = base_input()
    input_data["age"] = 30

    response = LifeRisk(input_data).evaluate()

    assert response == REGULAR
