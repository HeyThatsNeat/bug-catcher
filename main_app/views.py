from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Bug


def bug_index(request):
  bugs = Bug.objects.all()
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def bug_detail(request, bug_id):
  bug = Bug.objects.get(id=bug_id)
  return render(request, 'bugs/detail.html', { 'bug': bug })

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')