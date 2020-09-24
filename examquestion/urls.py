
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.mathExamIndex, name='mathexamindex'),
    path('math1/', views.mathExam1, name="mathexam1"),

] 