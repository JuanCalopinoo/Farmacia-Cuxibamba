
from django.shortcuts import render, get_object_or_404 , redirect

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def re(request):
    return render(request, 're.html')