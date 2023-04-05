from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routes import temperature_router, wind_velocity_router

app = FastAPI()

app.include_router(temperature_router)
app.include_router(wind_velocity_router)

TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
        }
    },
}

register_tortoise(
    app, config=TORTOISE_ORM, generate_schemas=True, add_exception_handlers=True
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
