from django.shortcuts import render
from .models import Bug


def bug_index(request):
  bugs = Bug.objects.all()
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')