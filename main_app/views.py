from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'Java Sparrow','pink belly, white-cheeked black head, red eye-ring', 3),
  Finch('Stich', 'Diamond Firetail', 'plump', 0),
  Finch('Moana', 'The Gouldian Finch', 'rainbow finch', 4)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello home /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })

