from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
  print(args, kwargs)
  print(request.user) # access the curr user
  # return HttpResponse("<h1>Hello World</h1>") # a string of HTML code
  return render(request, "home.html", {})
  
def contact_view(request, *args, **kwargs):  # *args, **kwargs
  # return HttpResponse("<h1>Contact Page</h1>") # a string of HTML code
  return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):  # *args, **kwargs
  my_context = {
    "title": "this is about us",
    "this_is_true": True,
    "my_number": "123",
    "my_list": [123, 234, 345],
    "my_html": "<h1>Hello world</h1>"
  }
  return render(request, "about.html", my_context)
