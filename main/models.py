from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории")
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-created_at"]

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self) -> str:
        return f"{self.name}, {self.price}, {self.category.name}"
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"



class NotificationProduct(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self) -> str:
        return f"User: {self.user.username},\n Product: {self.product.name}"
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"
        ordering = ["-created_at"]


class NotificationCategory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self) -> str:
        return f"User: {self.user.username},\n Category: {self.category.name}"
    
    class Meta:
        verbose_name = "Уведомление Category"
        verbose_name_plural = "Уведомления Category"
        ordering = ["-created_at"]

    
    


    