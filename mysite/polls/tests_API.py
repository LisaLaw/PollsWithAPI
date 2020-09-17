from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from polls.models import Question

class QuestionTest(APITestCase):
    def setUp(self):
        self.question = Question()

    def test_create_question(self):
        questions = Question.objects.all()
        data = {"question_text": "new question text"}
        response = self.client.post("api-root/questions/", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_created)
        question = Question.objects.get(question_text=data["question_text"])

    def test_question_text_is_not_empty(self):
        question_text = Question.question_text
        self.assertFalse(question_text='')