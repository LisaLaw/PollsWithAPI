from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.test import Client

from polls.models import Question
from django.contrib.auth.models import User

class QuestionTest(APITestCase):
    def setUp(self):
        self.question = Question() #now I can use question as an instance of the Model Question
        #create a user to prevent authorization error
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        #authenticate client with user
        self.client = Client()
        self.client.login(username=user.username, password='johnpassword')

    def test_question_is_created(self):
        questions = Question.objects.all().count() #get all Question instances and count them
        data = {"question_text": "new question text"} #data that the new question has
        response = self.client.post('/questions/', data=data, format="json") #user adds a questions in url "questions/" with the question text form above. Get back the result in json
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) #check if status code of the new question equals 201
        self.assertEqual(questions + 1, Question.objects.all().count()) #check if all Question instances have augmented by 1 (a new question has been created)

    def test_question_text_is_not_empty(self):
        question_text = Question('question_text') #get the question text for all questions
        self.assertIsNot(question_text, '') #checks that question text isn't empty
        