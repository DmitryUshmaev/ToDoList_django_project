from django.urls import path

from core.views import UserRegistrationView, UserLoginView, ProfileView

urlpatterns = [
    path('signup', UserRegistrationView.as_view()),
    path('login', UserLoginView.as_view()),
    path('profile', ProfileView.as_view()),
]