## Weather API

This is a simple RESTful API for managing temperature and wind velocity data. The API is built using Python, FastAPI, Tortoise ORM, and SQLite3. The API provides endpoints for creating, reading, updating, and deleting temperature and wind velocity data.

### Endpoints

The following endpoints are currently available:

- **POST /temperature** - Create a new temperature data entry
- **GET /temperature** - Retrieve a list of all temperature data entries
- **GET /temperature/{id}** - Retrieve a single temperature data entry by ID
- **PUT /temperature/{id}** - Update a single temperature data entry by ID
- **DELETE /temperature/{id}** - Delete a single temperature data entry by ID
- **POST /wind_velocity** - Create a new wind velocity data entry
- **GET /wind_velocity** - Retrieve a list of all wind velocity data entries
- **GET /wind_velocity/{id}** - Retrieve a single wind velocity data entry by ID
- **PUT /wind_velocity/{id}** - Update a single wind velocity data entry by ID
- **DELETE /wind_velocity/{id}** - Delete a single wind velocity data entry by ID

### Technologies Used

- Python 3.9
- FastAPI
- Tortoise ORM
- SQLite3

### How to Use

To use this API, you can clone this repository and set up a virtual environment. You can use the following commands to clone and set up the environment:

#### Windows

`$ git clone https://github.com/altns/fastapi-weather.git`

`$ cd weather-api`

`$ python3 -m venv env`

`$ venv\Scripts\activate`

`$ pip install -r requirements.txt`

#### macOS/Linux

`$ git clone https://github.com/altns/fastapi-weather.git`

`$ cd weather-api`

`$ python3 -m venv env`

`$ source env/bin/activate`

`$ pip install -r requirements.txt`

Once you have set up the environment, you can start the API server with the following command:

`$ uvicorn main:app --reload`

You can access the API documentation at `http://localhost:8000/docs` and the API endpoints at `http://localhost:8000/temperature` and `http://localhost:8000/wind_velocity`.

To test the API endpoints, we recommend using a REST API client such as Insomnia.

### License

This project is licensed under the terms of the MIT license. See [LICENSE](https://github.com/altns/fastapi-weather/blob/master/LICENSE) for more information.
