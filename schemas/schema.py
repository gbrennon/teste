from schematics import Model
from schematics.types import StringType, ListType, IntType, ModelType, BooleanType


class HouseModel(Model):
    ownership_status = StringType(required=False, serialized_name="ownership_status", choices=["owned", "mortgaged"])


class VehicleModel(Model):
    year = IntType(required=False, serialized_name="year")


class InputModel(Model):
    age = IntType(required=True, serialized_name="age", min_value=0)
    dependents = IntType(required=True, serialized_name="dependents", min_value=0)
    house = ModelType(model_spec=HouseModel, required=True, serialized_name="house")
    income = IntType(required=True, serialized_name="income", min_value=0)
    marital_status = StringType(required=True, serialized_name="marital_status", choices=["single", "married"])
    risk_questions = ListType(required=True, serialized_name="risk_questions", field=BooleanType, min_size=3,
                              max_size=3)
    vehicle = ModelType(model_spec=VehicleModel, required=True, serialized_name="vehicle")

