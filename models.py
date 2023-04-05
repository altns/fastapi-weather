from tortoise import fields
from tortoise.models import Model


class Temperature(Model):
    id = fields.IntField(pk=True)
    value = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)


class WindVelocity(Model):
    id = fields.IntField(pk=True)
    value = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)