from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'Favitude/index.html')  

def about(request):
  return render(request, 'Favitude/about.html')


def login_page(request):
  
  return render(request, 'Favitude/login.html')
def home_page(request):
  
  return render(request, 'Favitude/home.html')


def signup_page(request):
  return render(request, 'Favitude/signup.html')  

def contact_page(request):
  return render(request, 'Favitude/contact.html')

def error_page(request):
  return render(request, 'Favitude/error.html')

def generate_page(request):
  return render(request, 'Favitude/generate.html')

def imageGen_page(request):
  return render(request, 'Favitude/imageGen.html')         

def documentation_page(request):
  return render(request, 'Favitude/documentation.html')  

def tutorial_page(request):
  return render(request, 'Favitude/tutorial.html')   

def gen_from_text_page(request):
  return render(request, 'Favitude/gen_from_text.html')     

def privacy_page(request):
  return render(request, 'Favitude/privacy.html')       

def FAQs_page(request):
  return render(request, 'Favitude/FAQs.html')   