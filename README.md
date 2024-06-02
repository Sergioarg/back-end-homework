# Movies API Documentation

## Overview

This documentation outlines how to set up and use the Movies API, a Django backend designed for get and manage data of private and public movies.

## Getting Started

### Prerequisites

- Python 3.10.0 or higher
- Django 5.0.6 or higher
- Django REST framework 3.15.1 or higher

### Installation

1. Clone the repository:
    ```
    git clone https://github.com/Sergioarg/movies-api.git
    ```
2. Navigate to the project directory:
   ```
   cd users_api/
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
      ```
      .\venv\Scripts\activate
      ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```
6. Apply migrations to set up the database:
   ```
   python3 manage.py migrate
   ```
7. Create an admin user:
   ```
    python3 manage.py createsuperuser --username admin --email admin@example.com
   ```

## Running the Server

To start the server, run:
```
python manage.py runserver
```
The server will start at `http://localhost:8000`.

## API Endpoints

The API is structured around the following endpoints:

### Usage

To interact with the API, you can use tools like `curl`, Postman, or any HTTP client library in your preferred programming language.

Endpoint: `http://127.0.0.1:8000/api/users/login/`

- **Obtain API Token**
  - **Endpoint**: `/users/login/`
  - **Method**: `POST`
  - **Body**:
    ```json
    {
      "emial": "user@gmail.com",
      "password": "examplepassword"
    }
    ```
  - **Response**:
    ```json
    {
      "message": "Logged in successfully.",
      "token": "API-TOKEN"
    }
    ```

    - Curl Example:
    ```bash
    curl --location --request GET 'http://127.0.0.1:8000/api/movies/' \
    --header 'Authorization: Token <API-TOKEN>'
    ```

### Users Endpoints

- **Register a User**
  - **Endpoint**: `/api/users/register/`
  - **Method**: `POST`
  - **Body**:
    ```json
    {
        "email": "user@gmail.com",
        "password": "UserP@ssword123"
    }
    ```
  - **Response**:
    ```json
    {
      "email": "user@gmail.com",
    }
    ```

- **Login a User**
  - **Endpoint**: `/api/users/login/`
  - **Method**: `POST`
  - **Body**:
    ```json
    {
        "email": "user@gmail.com",
        "password": "UserP@ssword123"
    }
    ```
  - **Response**:
    ```json
    {
        "message": "Logged in successfully.",
        "token": "API-TOKEN"
    }
    ```
<!-- TODO: ADD DOCUMENTATION OF MOVIES ENDPOINT -->

### Run Tests
Execute the Django test runner to run all tests in the project.

```bash
python3 manage.py test
```
