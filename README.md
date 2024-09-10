## Learning Objectives

- The students should gain comprehensive knowledge of key Python libraries for GraphQL, namely Graphene.
- The students should be able to set up a development environment for creating GraphQL APIs using Python with the Graphene library.
- The students should be able to build a simple GraphQL API with Python and Flask.

### **Graphene**

https://docs.graphene-python.org/projects/sqlalchemy/en/latest/starter/

**Graphene** is a Python library for building GraphQL APIs in a simple yet powerful way. It provides a framework-agnostic approach, meaning you can integrate it seamlessly with various web frameworks such as Flask, Django, and more. Graphene allows you to define your schema using Python classes, making it easy to map Python objects to GraphQL types.

## Building our GraphQL API in Python

First as always, we want to set up a virtual environment and activate it

```
python -m venv venv
```

pip install the following requirements
```
Flask
Flask-Script
Flask-SQLAlchemy
Flask-GraphQL
graphene
graphene-sqlalchemy
PyMySQL
```

We're then going to start as if we were setting up a REST api, creating our app.py folder to run our app, and a models.py file to hold our database models

Makes sure to conigur your app's database uri to:

```
'mysql+pymysql://your_user:your_password@localhost/db_name'
```

In models.py we'll:
- set up our Base model
- Instantiate our db
- Create a Model for a Movie table in our db

Be sure to import and initialize our app on app.py
Also make sure to create_all() tables


In schemas.py:
    - Create a Movie Object Type using our Movie Model
    - Create a Query type to query for Movie Objects (will require a resolver to execute the query)
    - Create an AddMovie mutation, specifiying the Arguments, and interaction with the db
    - Create a Mutation Type to incorporate our AddMovie Mutation