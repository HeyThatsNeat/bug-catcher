from django.shortcuts import render
from .models import Bug


def bug_index(request):
  bugs = Bug.objects.all()
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def bug_detail(request, bug_id):
  bug = Bug.objects.get(id=bug_id)
  return render(request, 'bugs/detail.html', { 'bug': bug })

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')