from datetime import datetime
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Temperature(Model):
    id = fields.IntField(pk=True, default=0)
    value = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True, default=datetime.utcnow())


TemperatureSchema = pydantic_model_creator(Temperature, name="Temperature")


class WindVelocity(Model):
    id = fields.IntField(pk=True, default=0)
    value = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True, default=datetime.utcnow())


WindVelocitySchema = pydantic_model_creator(WindVelocity, name="WindVelocity")
