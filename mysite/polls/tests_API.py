from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from polls.models import Question

class QuestionTest(APITestCase):

    def test_question_text_is_not_empty(self):
        question_text = Question.question_text
        self.assertFalse(question_text='')