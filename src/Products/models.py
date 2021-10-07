from django.db import models

CATEGORY = [
    ('Electronics', ('Electronics')),
    ('Furniture', ('Furniture')),
    ('Toys', ('Toys')),
    ('Hardware', ('Hardware')),
    ('Medicine', ('Medicine')),
    ('Groceries', ('Groceries'))
]

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"