# Movies API Documentation

## Overview

This is a simple API that allows you to create, read, update and delete movies, and also allow you to filter their public and private movies.

**Deploy:** The API is deployed in Render, you can access here: [Movies API](https://movies-api-aw2p.onrender.com/).

*P.S:* The API also has documentation given by the swagger built-in in DRF.

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
2. Create a virtual environment *(optional but recommended)*:
   ```
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
      ```
      .\venv\Scripts\activate
      ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```
3. Install the required packages:
   ```
   pip3 install -r requirements.txt
   ```
4. Apply migrations to set up the database:
   ```
   python3 manage.py migrate
   ```
5. Create an admin user *(optional)*:
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

- **Get a random number**
  - **Endpoint**: `/api/number/`
  - **Description**: Returns a random number.
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
      "refresh": "YOUR-REFRESH-TOKEN",
      "access": "YOUR-ACCESS-TOKEN",
    }
    ```
  - Curl example to use of the access token:

    ```bash
    curl --request GET 'http://127.0.0.1:8000/api/movies/' \
    --header 'Authorization: Bearer <YOUR-ACCESS-TOKEN>'
    ```

### Movies Endpoints

You must have to make this request with your `YOUR-ACCESS-TOKEN` obtained previously.

- **Get private or public movies**
  - **Base Endpoint**: `/api/movies/`
    - **Description**: Returns all public movies created by others users and by the user.
  - **Custom Endpoints**: `/api/movies/private/` or  `/api/movies/public/` or `/api/movies/all/`
    - **Description**: These endpoints will return the movies created by the user based on the type of the request.
  - **Method**: `GET`
  - **Authtoken**: `Bearer <YOUR-ACCESS-TOKEN>`
  - **Response**:
    ```json
    [
      {
        "title": "Django Unchained",
        "description": "Django, an African slave, is freed by a German bounty hunter and becomes his apprentice.",
        "genre": "Action",
        "cast": "['Jamie Foxx', 'Leonardo DiCaprio']",
        "year": 2012,
        "original_lang": "en",
        "is_private": false, // or true
        "director": "Quentin Tarantino",
        "duration": "2:45:00"
      }
    ]
    ```

- **Create a Movie**
  - **Endpoint**: `/api/movies/`
  - **Authtoken**: `Bearer <YOUR-ACCESS-TOKEN>`
  - **Method**: `POST`
  - **Body**:
    ```json
    {
      "title": "Drive",
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

- **Update a Movie with `PUT`**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `PUT`
  - **Authtoken**: `Bearer <YOUR-ACCESS-TOKEN>`
  - **Body**:
    ```json
    {
      "title": "Drive",
      "description": "Update a movie description",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2011,
      "user": 1,
      "duration": "1:50:00",
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
      "genre": "Western",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2012,
      "original_lang": "en",
      "is_private": true,
      "director": "Nicolas Winding Refn",
      "duration": "1:50:00"
    }
    ```

- **Update a Movie with `PATCH`**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `PATCH`
  - **Authtoken**: `Bearer <YOUR-ACCESS-TOKEN>`
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
      "genre": "Western",
      "cast": ["Ryan Gosling", "Bryan Cranston"],
      "year": 2012,
      "original_lang": "en",
      "is_private": false,
      "director": "Nicolas Winding Refn",
      "duration": "1:50:00"
    }
    ```

- **Delete a Movie**
  - **Endpoint**: `/api/movies/1/`
  - **Method**: `DELETE`
  - **Authtoken**: `Bearer <YOUR-ACCESS-TOKEN>`
  - **Response**: `204 No Content`

### Run Tests
Execute the Django test runner to run all tests in the project.

```
$ python3 manage.py test

Found 30 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..............................
----------------------------------------------------------------------
Ran 30 tests in 4.894s

OK
Destroying test database for alias 'default'...
```
