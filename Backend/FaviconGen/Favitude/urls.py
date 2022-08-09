from django.urls import path
from . import views

urlpatterns = [
  path("about/", views.about, name="about_page"),
  path("login/", views.login, name="login_page"),
  path("signup/", views.signup, name="signup_page"),
]