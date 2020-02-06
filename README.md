# FSND Casting Agency Capstone project

## capstone project for the udacity full stack nanodegree program.

**Heroku link:** (https://capstone-fsnd.herokuapp.com/)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in api.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

To run the server, execute:

```
export FLASK_APP=api.py
export FLASK_ENV=debug
flask run --reload
```


## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Models

Movies with attributes contain title, year, director and genre
Actors with attributes name, role and gender

## Environment Variables

In the `.env` file, the JWT token for each User Role
- CASTING_ASSISTANT
- CASTING_DIRECTOR
- EXECUTIVE_PRODUCER

## Roles

Casting Assistant

- GET:actors
- GET:movies

Casting Director
#####  All permissions a Casting Assistant has
- POST:actor
- DELETE:actor
- PATCH:actor
- PATCH:movie

Executive Producer

##### All permissions a Casting Director has
- POST:movie
- DELETE:movie

## Endpoints

`````bash
GET '/actors'

reponse = {
success: True,
actors: [
          {
            name: "Kelvin Hart",
            role: "cast",
            gender: "male",
          },
          {
            name: "Kelvin Hart",
            role: "cast",
            gender: "male",
          }
        ]
  }


POST '/actors'

payload = {
     name: "Kelvin Hart",
    role: "cast",
    gender: "male",
  }
response = {
  success: True,
  actor:{  
    name: "Kelvin Hart",
    role: "cast",
    gender: "male"
   }
}

PATCH '/actors/<int:actor_id>'

params = <int:actor_id>

response = {
  success: True,
  actor:{  
    name: "Kelvin Hart",
    role: "cast",
    gender: "male"
   }
}

DELETE '/actors/<int:actor_id>'

params = <int:actor_id>

response = {
  success: True,
  delete: actor_id
}

GET '/movies'

response = {
success: True,
movies: [
          {
            title: "Avengers",
            year: 2019,
            director: "Kenny Faggie",
            genre: "fiction"
          },
          {   
            title: "Avengers",
            year: 2019,
            director: "Kenny Faggie",
            genre: "fiction"
          }
        ]
  }


POST '/movies'

payload = {
   title: "Avengers",
    year: 2019,
    director: "Kenny Faggie",
    genre: "fiction"
  }
response = {
  success: True,
  movie: {
     title: "Avengers",
    year: 2019,
    director: "Kenny Faggie",
    genre: "fiction"
 }
}

PATCH '/movies/<int:movie_id>'

params = <int:movie_id>

response = {
success: True,
movies: {   
            title: "Avengers",
            year: 2019,
            director: "Kenny Faggie",
            genre: "fiction"
          }
        
  }


DELETE '/movies/<int:movie_id>'


params = <int:movie_id>

response = {
  success: True,
  delete: movie_id
} 

`````
## Testing

To run the tests, cd into `/src` and run in your terminal

```bash

python test.py
`````
