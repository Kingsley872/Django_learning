from django.db import models
from django.urls import reverse
# Create your models here.

# $ python manage.py makemigrations
# $ python manage.py migrate
# these two command we should do each time we make changes in modles.py

# python shell command line add Product:
# $ python manage.py shell
# $ from products.modles import Porduct
# $ Product.objects.all() // get all objects in current table
# $ Prodect.objects.create(title='something', description='somedes', price='123', summary='ok')

class Product(models.Model): 
  title       = models.CharField(max_length=120) # max_length is required
  description = models.TextField(blank=True, null=True)
  price       = models.DecimalField(decimal_places=2, max_digits=1000)
  summary     = models.TextField(blank=True, null=False) # blank=True means this field can be empty
  featured    = models.BooleanField(default=False) # null=True, defualt=True

  def get_absolute_url(self):
    # return f"/dynamic/{self.id}"
    return reverse("products:product-detail", kwargs={"id": self.id}) # the link dynamicly bound with the revese function which is basd on the name of the url and the id whichi represents to the product id 