# investingApp

Students: Daniel-Tiberiu Bociat and Amir-Ali Azhari

This project was done for the Software Engineering Fundamentals laboratory - The Polytechnic University of Timisoara, year 2, faculty of Automation and Computing.

The project was done using Django and its purpose was to learn the framework as well as working in a team, working with Git and Jira. It is not meant to be a realistic application.

# Prerequisites

Installing [python](https://phoenixnap.com/kb/how-to-install-python-3-windows) and [pip](https://phoenixnap.com/kb/install-pip-windows).

To install Django use the command __python -m pip install Django__.

The official Django tutorial can be found [here](https://docs.djangoproject.com/en/3.2/topics/install/). 

# Starting the Application

To run the application the command __python manage.py runserver__ should be run in the project folder, in our case in investingApp.

If there are no errors the application can be accesed at the address [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# Possible errors and fixes

If there were changes at the __models.py__ a migration might be needed.

Use the commands: __python manage.py makemigrations__ and __python manage.py migrate__

If a hard reset of the database is needed deletete the contents of the migrations file from all the applications __EXCEPT__ the \_\_init\_\_.py files, delete the database db.sqlite3, and finally run the commands above.

# Testing the application

To run the tests for the project run the command __python manage.py test__ or __python manage.py test <app_name>__ to run the test for a specific app.

In our case only there are only tests in the authentication app which test the database models.

# Creating a superuser

To create a superuser run the command __python manage.py createsuperuser__ and pick and email and password for the superuser.

The superuser has access to the admin page [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) where it can see the data in the databases, as well as adding, deleting and modifying entries.

# Using the application

There are two types of users: investors and companies, each with their own registration page but common login page.

Each company has a stock with a buying price and a selling price.

Companies can add/remove available shares and can see the current number of shares and the buying/selling price.

Investors can deposit/withdraw money, buy/sell shares and see their current free funds and account value which sums the free funds and all the shares owned.
