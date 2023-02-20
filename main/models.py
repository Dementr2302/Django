from django.db import models
from users.models import User
# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True) # макс длина 128 / уникальное
    discription = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)                         # название
    discription = models.TextField()                                # описание
    price = models.DecimalField(max_digits=6, decimal_places=2)     # цена  # цифры до запятой и после
    quantity = models.PositiveIntegerField(default=0)               # количество товаров на складе / по умолчанию 0 товаров
    image = models.ImageField(upload_to='products_img')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)   # связываем с другой таблицей / удаляестя
                                                                                # категория и все товары , лучше исп (Protect)
    def __str__(self):
        return f'Продукт: {self.name} | Категория {self.category}'

class Basket(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity