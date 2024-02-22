from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50,default="")
    price = models.DecimalField(max_digits=5, decimal_places=2 , default = 0)
    description = models.CharField(max_length= 2000)
    link = models.ImageField( upload_to='Views/media/images')
    review = models.IntegerField(default=0)
    ingredient = models.CharField(default = " ", max_length=200 , blank = True)
    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    time = models.DateTimeField(default = timezone.now, editable=False)
    quantity = models.IntegerField(default = 0)
    paid = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} purchased at {self.time}"