from django.db import models
from django.utils import timezone
from accounts.models import Customer


class Reward(models.Model):
    sku = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    points_cost = models.IntegerField()
    stock = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=64)
    image_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.sku} - {self.name}"


class Redemption(models.Model):
    STATUS_PENDING = "PENDING"
    STATUS_CONFIRMED = "CONFIRMED"
    STATUS_CANCELED = "CANCELED"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="redemptions")
    total_points = models.IntegerField()
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self) -> str:
        return f"Redemption#{self.id} {self.customer_id} {self.total_points}"


class RedemptionItem(models.Model):
    redemption = models.ForeignKey(Redemption, on_delete=models.CASCADE, related_name="items")
    reward = models.ForeignKey(Reward, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    points_each = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.reward_id} x{self.quantity}"

# Create your models here.
