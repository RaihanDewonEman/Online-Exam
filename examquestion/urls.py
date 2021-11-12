
from django.urls import path, include
from . import views

urlpatterns = [

    path('mathindex/', views.mathExamIndex, name='mathexamindex'),
    path('math1/', views.mathExam1, name="mathexam1"),
    path('banglaindex/', views.banglaExamIndex, name='banglaexamindex'),
    path('bangla1/', views.banglaExam1, name="banglaexam1"),

] 