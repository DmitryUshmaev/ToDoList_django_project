from django.urls import path

from core.views import UserCreateView

urlpatterns = [
    path('create/', UserCreateView.as_view()),
]