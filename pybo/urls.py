from django.urls import path
from . import views

# from .models import Question

urlpatterns = [
    path("", views.index),
    path("<int:question_id>/", views.detail),
]