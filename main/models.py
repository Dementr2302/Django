from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True) # макс длина 128 / уникальное
    discription = models.TextField(null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)                         # название
    discription = models.TextField()                                # описание
    price = models.DecimalField(max_digits=6, decimal_places=2)     # цена  # цифры до запятой и после
    quantity = models.PositiveIntegerField(default=0)               # количество товаров на складе / по умолчанию 0 товаров
    image = models.ImageField(upload_to='products_img')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)   # связываем с другой таблицей / удаляестя
                                                                                # категория и все товары , лучше исп (Protect)

