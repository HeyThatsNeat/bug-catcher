from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


# Add the Cat class & list and view function below the imports
class Bug:  # Note that parens are optional if not inheriting from another class
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
# Define the home view
# Add new view
def bug_index(request):
  return render(request, 'bugs/index.html', { 'bugs': bugs })

def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')