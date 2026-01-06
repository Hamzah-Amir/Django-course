from django.db import models
from uuid import uuid4

# Create your models here.

class Product(models.Model): 
    seller = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='products')
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    category = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name