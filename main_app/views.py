from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Bug

@login_required
def bug_index(request):
  bugs = Bug.objects.filter(user=request.user)
  return render(request, 'bugs/index.html', { 'bugs': bugs })

@login_required
def bug_detail(request, bug_id):
  bug = Bug.objects.get(id=bug_id)
  return render(request, 'bugs/detail.html', { 'bug': bug })

class Home(LoginView):
  template_name = 'home.html'

class BugCreate(LoginRequiredMixin, CreateView):
  model = Bug
  fields = ['subject', 'language', 'bugged_Code', 'fixed_Code']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BugUpdate(LoginRequiredMixin, UpdateView):
  model = Bug
  fields = ['language', 'bugged_Code', 'fixed_Code']

class BugDelete(LoginRequiredMixin, DeleteView):
  model = Bug
  success_url = '/bugs/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('bug-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def about(request):
  return render(request, 'about.html')