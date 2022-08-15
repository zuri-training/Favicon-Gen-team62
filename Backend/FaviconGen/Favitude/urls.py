from django.urls import path
from . import views

app_name = "Favitude"

urlpatterns = [
  path("", views.home, name="home_page"),
  path("about/", views.about, name="about_page"),
  path("login/", views.login_page, name="login_page"),
  path("home/", views.home_page, name="home_page"),
  path("signup/", views.signup_page, name="signup_page"),
  path("contact/", views.contact_page, name="contact_page"),
  path("error/", views.error_page, name="error_page"),
  path("generate/", views.generate_page, name="generate_page"),
  path("imageGen/", views.imageGen_page, name="imageGen_page"),
  path("documentation/", views.documentation_page, name="documentation_page"),
  path("tutorial/", views.tutorial_page, name="tutorial_page"),
  path("gen_from_text/", views.gen_from_text_page, name="gen_from_text_page"),
  path("privacy/", views.privacy_page, name="privacy_page"),
  path("FAQs/", views.FAQs_page, name="FAQs_page"),
  
]