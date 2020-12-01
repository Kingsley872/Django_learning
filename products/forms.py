from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class ProductForm(forms.ModelForm):
    
  title       = forms.CharField(label='', widget=forms.TimeInput(attrs={"placeholder": "You title"}))
  # email       = forms.EmailField()
  description = forms.CharField(
    required=False, 
    widget=forms.Textarea(attrs={
      "placeholder": "You description",
      "class": "new-class-name two",
      "id": "my-id-for-textarea",
      "row": 20,
      "col": 100,
    })
   ) # the fild is required to fill in 
  price       = forms.DecimalField(initial=199.99) # initial value for pric

  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price',
    ]

  # def clean_title(self, *args, **kwargs):
  #   title = self.cleaned_data.get("title")
  #   if not "CFE" in title:
  #     raise forms.ValidationError("This is not a valid title")
  #   return title # for defualt

  # def clean_email(self, *args, **kwargs):
  #   email = self.cleaned_data.get("email")
  #   if not email.endswith("edu"):
  #     raise forms.ValidationError("This is not a valid email")
  #   return email 

class RawProductForm(forms.Form):
  title       = forms.CharField(label='', widget=forms.TimeInput(attrs={"placeholder": "You title"}))
  description = forms.CharField(
    required=False, 
    widget=forms.Textarea(attrs={
      "placeholder": "You description",
      "class": "new-class-name two",
      "id": "my-id-for-textarea",
      "row": 20,
      "col": 100,
    })
   ) # the fild is required to fill in 
  price       = forms.DecimalField(initial=199.99) # initial value for price