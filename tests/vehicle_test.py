from handlers.risk_score_processor import ECONOMIC, REGULAR
from handlers.risk_score_processor.auto import AutoRisk
from tests import base_input


def test_auto_last_5_year():
    input_data = base_input()
    input_data["vehicle"]["year"] = 2015

    response = AutoRisk(input_data).evaluate()

    assert response == REGULAR


def test_auto_over_5_year():
    input_data = base_input()
    input_data["vehicle"]["year"] = 2014

    response = AutoRisk(input_data).evaluate()

    assert response == ECONOMIC
