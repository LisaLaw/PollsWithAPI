from rest_framework import serializers
from polls.models import Question, Choice
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Question
        fields = ['url', 'id', 'question_text', 'pub_date', 'owner']

class ChoiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Choice
        fields = ['url', 'id', 'choice_text', 'owner']

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    choices = serializers.PrimaryKeyRelatedField(many=True, queryset=Choice.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'questions', 'choices']