from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=32, unique=True)
    country = models.CharField(max_length=2)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.full_name or self.user.username

# Create your models here.
