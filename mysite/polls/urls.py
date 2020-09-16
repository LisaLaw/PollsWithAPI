from django.urls import path, include
from . import viewsets
from .viewsets import QuestionViewSet, UserViewSet, ResultsViewSet
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'questions', viewsets.QuestionViewSet)
router.register(r'users', viewsets.UserViewSet)
router.register(r'results', viewsets.ResultsViewSet)

urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', include(router.urls)),
]