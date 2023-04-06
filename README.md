### Clone the repository

1.  Open a terminal or command prompt
2.  Navigate to the directory where you want to store the project
3.  Run the following command to clone the repository:

    `https://github.com/altns/fastapi-weather`

### Set up virtual environment

1.  Navigate into the project directory
2.  Create a new virtual environment by running the following command:
    `python -m venv venv`
3.  Activate the virtual environment by running the following command:

    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`

### Install dependencies

1.  Ensure that you have `pip` installed by running the following command:
    `python -m pip install --upgrade pip`
2.  Install the project dependencies by running the following command:
    `pip install -r requirements.txt`

### Set up the database

1.  Open the `settings.py` file in the project directory
2.  Configure the database settings according to your own setup
3.  Run the following command to create the database tables:
    `python app/db.py`

### Start the server

1.  Run the following command to start the server

    `uvicorn app.main:app --reload`

2.  Open a web browser and navigate to `http://localhost:8000/docs`. This will open the Swagger UI, where you can test the API endpoints.
