from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Bug


def bug_index(request):
  bugs = Bug.objects.filter(user=request.user)
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def bug_detail(request, bug_id):
  bug = Bug.objects.get(id=bug_id)
  return render(request, 'bugs/detail.html', { 'bug': bug })

class Home(LoginView):
  template_name = 'home.html'

# class BugCreate(CreateView):
#   model = Bug
#   fields = ['name', 'breed', 'description', 'age']
  
#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cat-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def about(request):
  return render(request, 'about.html')