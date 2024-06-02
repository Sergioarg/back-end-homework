# Movies API Documentation

## Overview

This is a simple API that allows you to create, read, update and delete movies, and also allow you to filter their public and private movies.

**P.S:** The API also has documentation given by the swagger integrated in DRF, this readme is an overview.

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

### Random Number Enpoint

- **Register a User**
  - **Endpoint**: `/api/number/`
  - **Description**: Returns a random number between 1 and 10.
  - **Authtoken**: No authtoken required.
  - **Method**: `GET`
  - **Response**:
    ```json
    {
      "number": 8,
    }
    ```

### Users Endpoints

- **Register a User**
  - **Endpoint**: `/api/users/register/`
  - **Authtoken**: No authtoken required.
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

- **Login a User and Obtain API Token**
  - **Endpoint**: `/api/users/login/`
  - **Authtoken**: No authtoken required.
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
    - Curl example to use of the token:

    ```bash
    curl --location --request GET 'http://127.0.0.1:8000/api/movies/' \
    --header 'Authorization: Token <API-TOKEN>'
    ```

### Movies Endpoints

You must have to make this request with your `API-TOKEN` obtained previously.

- **Get private or public movies**
  - **Endpoints**: `/api/movies/private` or `/api/movies/public`
  - **Method**: `GET`
  - **Description**: These endpoints will return the movies created by the user based on the type of the request.
  - **Authtoken**: Authtoken required.
  - **Response**:
    ```json
    [
      {
        "title": "Driver",
        "description": "Driver movie starring Ryan Gosling",
        "genre": "Action",
        "cast": "['Ryan Gosling', 'Bryan Cranston']",
        "year": 2011,
        "original_lang": "en",
        "is_private": false, // or true
        "director": "Nicolas Winding Refn",
        "duration": "3:00:00"
      }
    ]
    ```

- **Create a Movie**
  - **Endpoint**: `/api/movies/`
  - **Authtoken**: Authtoken required.
  - **Method**: `POST`
  - **Body**:
    ```json
    {
      "title": "Taxi",
      "description": "A stuntman and getaway driver falls in love with Irene who is married to a criminal.",
      "cast": ["Ryan Gosling", "Carey Mulligan", "Bryan Cranston"],
      "year": 2011,
      "user": 1, // Your user id
      "duration": 100,
      "original_lang": "en",
      "genre": "Action",
      "is_private": false,
      "director": "Nicolas Winding Refn"
    }
    ```
  - **Response**:
    ```json
    {
      "title": "Drive",
      "description": "A stuntman and getaway driver falls in love with Irene who is married to a criminal.",
      "genre": "Action",
      "cast": [
          "Ryan Gosling",
          "Carey Mulligan",
          "Bryan Cranston"
      ],
      "year": 2011,
      "original_lang": "en",
      "is_private": false,
      "director": "Nicolas Winding Refn",
      "duration": "1:40:00"
    }
    ```

- **Update a Movie `PUT`**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `PUT`
  - **Authtoken**: Authtoken required.
  - **Body**:
    ```json
    {
      "title": "Drive",
      "description": "Update a movie description",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2011,
      "user": 1,
      "duration": 110,
      "original_lang": "en",
      "genre": "Action",
      "is_private": true,
      "director": "Nicolas Winding Refn"
    }
    ```
  - **Response**:
    ```json
    {
      "title": "Drive",
      "description": "Update a movie description",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2011,
      "user": 1,
      "duration": 110,
      "original_lang": "en",
      "genre": "Action",
      "is_private": true,
      "director": "Nicolas Winding Refn"
    }
    ```

- **Update a Movie with `PATCH`**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `PATCH`
  - **Authtoken**: Authtoken required.
  - **Body**:
    ```json
    {
      "is_private": false,
    }
    ```
  - **Response**:
    ```json
    {
      "title": "Drive",
      "description": "Update a movie description",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2011,
      "user": 1,
      "duration": 110,
      "original_lang": "en",
      "genre": "Action",
      "is_private": false,
      "director": "Nicolas Winding Refn"
    }
    ```

- **Update a Movie `PATCH`**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `PATCH`
  - **Authtoken**: Authtoken required.
  - **Body**:
    ```json
    {
      "is_private": false,
    }
    ```
  - **Response**:
    ```json
    {
      "title": "Drive",
      "description": "Update a movie description",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2011,
      "user": 1,
      "duration": 110,
      "original_lang": "en",
      "genre": "Action",
      "is_private": false,
      "director": "Nicolas Winding Refn"
    }
    ```

- **Delete a Movie**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `DELETE`
  - **Authtoken**: Authtoken required.
  - **Response**: `204 No Content`

### Run Tests
Execute the Django test runner to run all tests in the project.

```bash
python3 manage.py test
```
