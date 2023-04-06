from fastapi import APIRouter, HTTPException
from typing import List

from models import Temperature, WindVelocity, TemperatureSchema, WindVelocitySchema
# from schemas import TemperatureSchema, WindVelocitySchema

temperature_router = APIRouter()
wind_velocity_router = APIRouter()


@temperature_router.post("/temperature", response_model=TemperatureSchema)
async def create_temperature(temperature: TemperatureSchema):
    temperature_obj = await Temperature.create(**temperature.dict())
    return await TemperatureSchema.from_tortoise_orm(temperature_obj)


@temperature_router.get("/temperature", response_model=List[TemperatureSchema])
async def get_all_temperatures():
    return await TemperatureSchema.from_queryset(Temperature.all())


@temperature_router.get("/temperature/{id}", response_model=TemperatureSchema)
async def get_temperature(id: int):
    try:
        temperature_obj = await Temperature.get(id=id)
        return await TemperatureSchema.from_tortoise_orm(temperature_obj)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Temperature not found")


@temperature_router.put("/temperature/{id}", response_model=TemperatureSchema)
async def update_temperature(id: int, temperature: TemperatureSchema):
    try:
        await Temperature.filter(id=id).update(**temperature.dict())
        temperature_obj = await Temperature.get(id=id)
        return await TemperatureSchema.from_tortoise_orm(temperature_obj)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Temperature not found")


@temperature_router.delete("/temperature/{id}", response_model=dict)
async def delete_temperature(id: int):
    deleted_count = await Temperature.filter(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Temperature not found")
    return {"deleted": deleted_count}


@wind_velocity_router.post("/wind_velocity", response_model=WindVelocitySchema)
async def create_wind_velocity(wind_velocity: WindVelocitySchema):
    wind_velocity_obj = await WindVelocity.create(**wind_velocity.dict())
    return await WindVelocitySchema.from_tortoise_orm(wind_velocity_obj)


@wind_velocity_router.get("/wind_velocity", response_model=List[WindVelocitySchema])
async def get_all_wind_velocities():
    return await WindVelocitySchema.from_queryset(WindVelocity.all())


@wind_velocity_router.get("/wind_velocity/{id}", response_model=WindVelocitySchema)
async def get_wind_velocity(id: int):
    try:
        wind_velocity_obj = await WindVelocity.get(id=id)
        return await WindVelocitySchema.from_tortoise_orm(wind_velocity_obj)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Wind velocity not found")


@wind_velocity_router.put("/wind_velocity/{id}", response_model=WindVelocitySchema)
async def update_wind_velocity(id: int, wind_velocity: WindVelocitySchema):
    try:
        await WindVelocity.filter(id=id).update(**wind_velocity.dict())
        wind_velocity_obj = await WindVelocity.get(id=id)
        return await WindVelocitySchema.from_tortoise_orm(wind_velocity_obj)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Wind velocity not found")


@wind_velocity_router.put("/wind_velocity/{id}", response_model=WindVelocitySchema)
async def update_wind_velocity(id: int, wind_velocity: WindVelocitySchema):
    await WindVelocity.filter(id=id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail="Wind velocity not found")
    return {"deleted": deleted_count}
