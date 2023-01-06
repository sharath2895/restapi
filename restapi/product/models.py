from django.db import models


# Create your models here.

class ProductModel(models.Model):
    id = models.UUIDField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    seller_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
