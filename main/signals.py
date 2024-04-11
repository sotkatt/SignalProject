from random import choice

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import (
    Product, NotificationProduct, Category, NotificationCategory
)


@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        users = User.objects.filter(is_superuser=True)
        NotificationProduct.objects.create(
            user = choice(users), 
            product = instance
        )


@receiver(post_save, sender=Category)
def create_category(sender, instance, created, **kwargs):
    if created:
        users = User.objects.filter(is_superuser=True)
        NotificationCategory.objects.create(
            user = choice(users),
            category = instance
        )


