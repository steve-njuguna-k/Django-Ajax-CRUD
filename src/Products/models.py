from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.name