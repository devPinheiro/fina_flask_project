import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import setup_db, Actor, Movie
from .auth.auth import AuthError, requires_auth
app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
# db_drop_and_create_all()

# Set up CORS


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# ROUTES

@app.route('/actors')
def get_actors():
    try:
        all_actors = Actor.query.order_by(Actor.id).all()

        if len(all_actors) == 0:
            abort(404)

        actors = [{"name": actor.name, "role": actor.role,
                   "gender": actor.gender}
                  for actor in all_actors]

        return jsonify({
            'success': True,
            'actors': actors,
        }), 200
    except Exception:
        abort(422)


'''
@TODO implement endpoint
    POST /actors
        it should create a new row in the actors table
        it should require the 'post:actors' permission
        it should contain the actor.long() data representation
    returns status code 200 and json {"success": True, "actors": actor}
    where actor an array containing only the newly created actor
        or appropriate status code indicating reason for failure
'''


@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def createactor(self):

    body = request.get_json()
    new_name = body.get('name', None)
    new_role = body.get('role', None)
    new_gender = body.get('gender', None)

    if new_name is None:
        abort(400)
    try:
        actor = Actor(name=new_name, role=new_role, gender=new_gender)
        actor.insert()
        new_act = actor.format()

        return jsonify({
            'success': True,
            'actors': new_act,
        }), 200
    except Exception:
        abort(422)


'''
@TODO implement endpoint
    PATCH /actors/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:actors' permission
    returns status code 200 and json {"success": True, "actors": actor}
    where actor an array containing only the updated actor
        or appropriate status code indicating reason for failure
'''


@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(self, actor_id):

    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

    if actor is None:
        abort(404)

    body = request.get_json()
    if body is None:
        abort(400)

    new_name = body.get('name', None)
    new_role = body.get('role', None)
    new_gender = body.get('gender', None)

    try:
        if new_name is not None:
            actor.name = new_name

        if new_gender is not None:
            actor.gender = new_gender

        actor.update()

        new_actor = [actor.format()]

        return jsonify({
            'success': True,
            'actors': new_actor,
        }), 200

    except Exception:
        abort(422)


'''
@TODO implement endpoint
    DELETE /actors/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:actors' permission
    returns status code 200 and json {"success": True, "delete": id}
    where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/actors/<int:actor_id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(self, actor_id):

    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

    if actor is None:
        abort(404)
        
    actor.delete()

    return jsonify({
        'success': True,
        'delete': actor_id,
    }), 200


# Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "message": error.error
    }), error.status_code
