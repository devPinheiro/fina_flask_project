import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from api import APP
from database.models import db
# print(os.environ['DATABASE_URI'])


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the CastingAgency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP
        self.client = self.app.test_client
        self.casting_assistant = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FRTVSRFpCUVRjMVFUYzBRVVF4TmpFd1FVWTBRek5DTmpVeE5ESkNNakZFUVRNeU5rSTVSQSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlM2EwNjkzZGFlMWUxMTFkMjY4MGQyOSIsImF1ZCI6Imh0dHA6bG9jYWxob3N0L2NhbGxiYWNsIiwiaWF0IjoxNTgwODYxMDgzLCJleHAiOjE1ODA4NjgyODMsImF6cCI6Ildqd3U3cDhxQk9IRWJMd0d3TUU1Mm51bEw5cEdyRmZmIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6W119.R937znTHLqlGeRo9t5zxbrIQOyiC25vRUCwsR9Iajqbym6n-whFGmqzl3GK6RWeHRa2InFY4744b3s37ov7vJrX3T50nRiDU5rpBYDYPrywuwMrG8Ehtoe-u4YDkS0O_4JCcX_ds5R0az4TOHgNvMCQdVJ8oHrZWz8Ek0bV4WqdTsPuaDItSA2UW8EkHGDvp82WpjrTh1qofxwxHZp2J43yI-ztfZw8nMYFD02VOZUFtujxuOVnaT2hqN7JfJ2bXdcCuAiIPBOpPJ3E_LDPQBOoQ2V25gGqvjadDQWPiTDWB4pZLnqgRRCiXpnfo5Cj3IN_ozYHuE_6BW8n_S_Pisw'
        self.casting_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FRTVSRFpCUVRjMVFUYzBRVVF4TmpFd1FVWTBRek5DTmpVeE5ESkNNakZFUVRNeU5rSTVSQSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlMzFhOWY2Nzc3NGQzMGQ5ZmUxMmJiNiIsImF1ZCI6Imh0dHA6bG9jYWxob3N0L2NhbGxiYWNsIiwiaWF0IjoxNTgwODYxMTI2LCJleHAiOjE1ODA4NjgzMjYsImF6cCI6Ildqd3U3cDhxQk9IRWJMd0d3TUU1Mm51bEw5cEdyRmZmIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.NQMeuq_tsjXLtSWcAyV3nTGBTjHKWUaEyabUg42k2HZKRxcNQ6DwKXdDy0gROdaTNkCMYVfaH0e2e8-nsQibqL9wLUHp17rUPaWtxecCUH299OlPW5qd5oCjVF6VKOr7odNiMvuLxV8huWRU24m3GMj_Io_Bfo7fmS_hrgZ8tuIUHm5fO5pO5LtxZyDZKNrZG6eRGfaw9E_hA4eJFVPj883BZyLJUV5dFFW_O_jYhKTDl1ya1BZiRTflq00-KDqFerVCsFi0IZPtI6vHdHeyIx2sstuZWLnQM5Z-glaX0r7qMRe8fx_QZKEareqBeHPzjNtwNJAuajgK6P97Xj1vUw'
        self.executive_director = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1FRTVSRFpCUVRjMVFUYzBRVVF4TmpFd1FVWTBRek5DTmpVeE5ESkNNakZFUVRNeU5rSTVSQSJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLXByb2plY3QuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlMzFhOTdhNzc3NGQzMGQ5ZmUxMmI4OCIsImF1ZCI6Imh0dHA6bG9jYWxob3N0L2NhbGxiYWNsIiwiaWF0IjoxNTgwODYxODgzLCJleHAiOjE1ODA4NjkwODMsImF6cCI6Ildqd3U3cDhxQk9IRWJMd0d3TUU1Mm51bEw5cEdyRmZmIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.kmSII3Edax18vQ8mBIWAylVFMEHdEkCsqSmG7eUuqFouNqS5ga7OLlqp9NUFDFeBesrdbdBLdvGWAYkbssQi0H-wnBX_IOZUUM3VqJpt3uK-Fj-HGVl1uukJmx6Zh582PogxF4X6iqFT-J4mZskEfm1VX77U6DqvzBjvH4GWzdXaCvc2tqzEp3O4JhV0caBK7SK3pN5643LbcEoPAR5N1QeSgZ_tgJi9yuuNsRFhaHNMoQbYus8c1hvy_dAGFkkuoNWUnJQgmgse-1iSdDu4LXz6VmVtYXzK16bpjXH7u4-n3TAQbe3xQjRfXahJw--FvOzREFp_Y-MJpsAZgdu-IA'
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
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
           # create all tables
            self.db.drop_all()
            self.db.create_all()

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
        self.assertEqual(data['actors'], {'gender': 'male', 'id': 1,
                                          'name': 'Kelvin Hart',
                                          'role': 'cast'})
   
    def delete_actor_casting_director(self):
        res = self.client().delete('/actors/1',
                                   headers={
                                       "Authorization": "Bearer {}".format(
                                           self.casting_assistant)
                                   })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # def test_fetch_all_questions(self):
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['categories'])
    #     self.assertTrue(data['questions'])

    # def test_get_category_question(self):
    #     res = self.client().get('/categories/2/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_category_non_existent_question(self):
    #     res = self.client().get('/categories/2345/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['message'], "unprocessable")
    #     self.assertEqual(data['success'], False)

    # def test_delete_question(self):
    #     res = self.client().delete('/questions/4')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)

    # def test_delete_non_existent_question(self):
    #     res = self.client().delete('/questions/236')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['message'], "unprocessable")
    #     self.assertEqual(data['success'], False)

    # def test_create_new_question(self):
    #     res = self.client().post('/questions', json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['created'])

    # def test_400_if_question_bad_request(self):
    #     res = self.client().post('/questions', json={})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'bad request')

    # def test_search_question(self):
    #     res = self.client().post('/questions/search',
    #                              json={"search_term": "what"})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_questions'])

    # def test_search_400_question_bad_request(self):
    #     res = self.client().post('/questions/search',
    #                              json={})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'bad request')

    # def test_get_quiz_non_existent(self):
    #     res = self.client().post('/quizzes',
    #                              json={
    #                                  "previous_questions": [],
    #                                  "quiz_category": 56
    #                              })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)

    # def test_get_quiz(self):
    #     res = self.client().post('/quizzes',
    #                              json={
    #                                  "previous_questions": [{
    #                                      "answer": "One",
    #                                      "category": 2,
    #                                      "difficulty": 4,
    #                                      "id": 18,
    #                                      "question": "How many paintings did "
    #                                      + "Van Gogh sell in his lifetime?"
    #                                  }],
    #                                  "quiz_category": 2
    #                              })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
        # self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
