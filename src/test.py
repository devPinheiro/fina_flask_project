import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from .database.models import setup_db, Actor, Movie, db


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the CastingAgency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.database_filename = "database_test.db"
        self.project_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = "sqlite:///{}".format(
        os.path.join(self.project_dir,
                     self.database_filename))
        db.init_app(self.app)
        # db.drop_all()
        db.create_all()
        

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

    """
    TODO
    Write at least one test for each test for successful
    operation and for expected errors.
    """

    def test_fetch_all_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        # self.assertTrue(data['categories'])

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
        self.assertEqual(data['success'], True)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
