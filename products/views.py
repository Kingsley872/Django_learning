from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, RawProductForm

from .models import Product


def product_create_view(request):
  form = ProductForm(request.POST or None)
  if form.is_valid():
    form.save()
    form = ProductForm() # rerender

  context = {
    'form': form
  }

  return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
  obj = get_object_or_404(Product, id=id)
  form = ProductForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
  context = {
    'form': form
  }
  return render(request, "products/product_create.html", context)

# list
def product_list_view(request):
  queryset = Product.objects.all() # give a list of objects 
  context = {
    "object_list": queryset
  }
  return render(request, "products/product_list.html", context)

# Create your views here.
def product_detail_view(request, id):
  obj = Product.objects.get(id=id)
  # context = {
  #   'title': obj.title,
  #   'description': obj.description,
  # }

  context = {
    'object': obj
  }
  return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
  obj = get_object_or_404(Product, id=id)
  if request.method == "POST":
    # confirming delete 
    obj.delete()
  context = {
    "object": obj
  }
  return render(request, "products/product_delete.html", context)




# dynamic url
def product_lookup_view(request, id):
  # obj = Product.objects.get(id=my_id)
  # obj = get_object_or_404(Product, id=id)
  try: # if the object id is not found then 404 not found page
    obj = Product.objects.get(id=id) # exception if there is no try block  
  except Product.DoesNotExist:
    raise Http404
  context = {
    "object": obj
  }
  return render(request, "products/product_detail.html", context)


# set initial data 
def render_initial_data(request):
  initial_data = {
    'title': "wholesome title"
  }
  obj = Product.objects.get(id=1)
  form = ProductForm(request.POST or None, instance=obj)
  if form.is_valid():
    form.save()
  context = {
    'form': form
  }
  return render(request, "products/product_create.html", context)

# def product_create_view(request):
#   my_form = RawProductForm()
#   if request.method == "POST":
#     my_form = RawProductForm(request.POST)
#     if my_form.is_valid():
#       # now the data is good
#       print(my_form.cleaned_data)
#       Product.objects.create(**my_form.cleaned_data)
#     else:
#       print(my_form.errors)
#   context = {
#     "form": my_form
#   }
#   return render(request, "products/product_create.html", context)


# def product_create_view(request):
#   # print(request.GET['title'])   using get to save data is unsafe method
#   # print(request.GET)
#   # print(request.POST)
#   if request.method == "POST":
#     my_new_title = request.POST.get('title')
#     print(my_new_title) # since requestion.method == "POST", there is no none in log 
#   context = {}
#   return render(request, "products/product_create.html", context)






