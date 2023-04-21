### 1. Create a virtual environment

### 2. Install packages : `pip install -r requirements.txt`

- (Database is Postgresql)

### 3. Setup .env file -

    Variables to set:
    - SECRET_KEY
    - DATABASE_NAME
    - DATABASE_USER
    - DATABASE_PASSWORD
    - DATABASE_HOST
    - DATABASE_PORT

### `python manage.py makemigrations`

### `python manage.py migrate`

### `python manage.py runserver`

###

### Then go to http://127.0.0.1:8000/docs to see all the api endpoints
