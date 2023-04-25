from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'home'

urlpatterns = [
    path('create', views.question_create.as_view()),
    path('question', views.question_list.as_view()),
    path('answer', views.QA_list.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)