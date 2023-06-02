from django.shortcuts import render


class Bug:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

bugs = [
  Bug('Lolo', 'tabby', 'Kinda rude.', 3),
  Bug('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Bug('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Bug('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def bug_index(request):
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')