from django.shortcuts import render

# Create your views here.
def about(request):
  return render(request, 'Favitude/about.html')


def login(request):
  return render(request, 'Favitude/login.html')


def signup(request):
  return render(request, 'Favitude/signup.html')  