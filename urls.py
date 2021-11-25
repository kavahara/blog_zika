from django.urls import path

from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activation/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('reset_password/', ResetPasswordView.as_view()),
    path('reset_password_complete/', ResetPasswordCompleteView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
]