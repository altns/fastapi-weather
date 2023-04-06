from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Temperature(Model):
    id = fields.IntField(pk=True)
    value = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

TemperatureSchema = pydantic_model_creator(Temperature, name="Temperature")

class WindVelocity(Model):
    id = fields.IntField(pk=True)
    value = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

WindVelocitySchema = pydantic_model_creator(WindVelocity, name="WindVelocity")