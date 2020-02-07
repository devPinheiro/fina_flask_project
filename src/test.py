import os
import unittest
import json
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from api import APP
from models import db
# print(os.environ['DATABASE_URI'])


# load env
load_dotenv()


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the CastingAgency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.testing = True
        self.client = self.app.test_client
        self.casting_assistant = os.getenv('CASTING_ASSISTANT')
        self.casting_director = os.getenv('CASTING_DIRECTOR')
        self.executive_producer = os.getenv('EXECUTIVE_PRODUCER')
        self.new_actor = {
            "name": "Kelvin Hart",
            "role": "cast",
            "gender": "male",
        }
        self.movies = {
            "title": "Avengers",
            "year": 2019,
            "director": "Kenny Faggie",
            "genre": "fiction"
        }
        db.drop_all()
        db.create_all()
        # binds the app to the current context
        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
        #    # create all tables
        #     self.db.drop_all()
        #     self.db.create_all()

    def tearDown(self):
        pass

    """
    TODO
    Write at least one test for each test for successful
    operation and for expected errors.
    """

    def test_fetch_all_actors_casting_assistant_first(self):
        res = self.client().get('/actors',
                                headers={
                                    "Authorization": "Bearer {}".format(
                                        self.casting_assistant)
                                })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_actor_casting_director(self):
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_director)
                                 }, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'], {'gender': 'male', 'id': 1,
                                          'name': 'Kelvin Hart',
                                          'role': 'cast'})

    def test_create_new_actor_executive_producer(self):
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.executive_producer)
                                 }, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'], {'gender': 'male', 'id': 1,
                                          'name': 'Kelvin Hart',
                                          'role': 'cast'})

    def test_create_new_actor_casting_assistant(self):
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_assistant)
                                 }, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], {
                         'code': 'unauthorized', 'description':
                         'Permission not found.'})
    
    def test_create_new_movies_executive_producer(self):
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.executive_producer)
                                 }, json=self.movies)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_movies_casting_assistant(self):
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_assistant)
                                 }, json=self.movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], {
                         'code': 'unauthorized', 'description':
                         'Permission not found.'})

    def test_create_new_movies_casting_director(self):
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer {}".format(
                                         self.casting_director)
                                 }, json=self.movies)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], {
                         'code': 'unauthorized', 'description':
                         'Permission not found.'})

        def test_fetch_all_moviess_casting_assistant_first(self):
            res = self.client().get('/movies',
                                    headers={
                                        "Authorization": "Bearer {}".format(
                                            self.casting_assistant)
                                    })
            data = json.loads(res.data)
            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'], False)
            self.assertEqual(data['message'], {
                'code': 'unauthorized', 'description':
                'Permission not found.'})


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
