from django.urls import path,include
from .views import *


urlpatterns=[
    path('one/<str:state_abb>/<str:election_cycle>/<str:election_round>/<int:ac_no>/',question_one),
    path('two/',QuestionTwo.as_view())
]