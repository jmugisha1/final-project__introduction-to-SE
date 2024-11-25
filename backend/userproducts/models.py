from django.db import models
from userauth.models import customUser

# Create your models here.
class userProduct(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productDate = models.DateField(auto_now_add=True)
    productImage = models.ImageField(upload_to='images/')
    productAuthor = models.ForeignKey(customUser, on_delete=models.CASCADE, related_name='userProduct')

    def __str__(self):
        return self.productName
    