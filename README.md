# Lord of the rings Character API

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development

* [SQLite](https://www.sqlite.org/index.html) : Application relational databases for development, staging and production environments
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment


## Description


## Getting Started

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/funsojoba/aspire_test_api.git` to clone the project repository.

Change directory into the project folder `cd aspire_test_api`, create and activate your virtual environment, install the required dependencies by running `pip install -r requirements.txt` after which you can make migrations and migrate by running `python manage.py makemigrations` and `python manage.py migrate`.

With these, you are ready to spin up your development server by running `python manage.py runserver` to get started. Your endpoint should be `127.0.0.1:8000` if your `port 8000` is not already in use


In summary, these are the lists of commands to run in listed order, to start up the project.

```
1. git clone https://github.com/funsojoba/aspire_test_api.git
2. cd aspire_test_api
3. python3 venv venv && source venv/bin/activate (activating virtual environment on a mac)
4. pip install -r requirements.txt
5. python manage.py makemigrations && python manage.py migrate
6. python manage.py runserver
```

## Swagger Documentation
Please visit `127.0.0.1:8000/swagger` for the swagger documentation of all endpoints.

## Running Tests

Unit test has been made available for various endpoints, you can run the test with the code below

```
python manage.py test
```

