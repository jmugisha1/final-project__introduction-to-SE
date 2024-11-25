from django.contrib import admin
# from django.contrib.admin.decorators import userAdmin

# Register your models here.
from .models import userProduct


class userProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'productName', 'productPrice', 'productDate', 'productAuthor')


admin.site.register(userProduct, userProductAdmin)