from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=200)
    productInfo = models.TextField(max_length=400)
    productPrice = models.IntegerField()
    productImage = models.FileField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.productName