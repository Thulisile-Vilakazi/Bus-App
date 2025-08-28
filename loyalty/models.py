from django.db import models
from django.utils import timezone
from accounts.models import Customer


class RemittanceTransaction(models.Model):
    CURRENCY_ZAR = "ZAR"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="remittances")
    amount_minor = models.BigIntegerField()
    currency = models.CharField(max_length=3, default=CURRENCY_ZAR)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self) -> str:
        return f"TX#{self.id} {self.customer_id} {self.amount_minor} {self.currency}"


class PointsReason(models.TextChoices):
    EARN_ON_REMITTANCE = "EARN_ON_REMITTANCE", "Earn on remittance"
    REDEMPTION = "REDEMPTION", "Redemption"
    ADJUSTMENT = "ADJUSTMENT", "Adjustment"
    ACHIEVEMENT = "ACHIEVEMENT", "Achievement"


class PointsLedger(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="points_ledger")
    delta = models.IntegerField()
    reason = models.CharField(max_length=32, choices=PointsReason.choices)
    reference = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ["-created_at", "-id"]


class Tier(models.Model):
    name = models.CharField(max_length=32, unique=True)
    min_lifetime_points = models.IntegerField()

    class Meta:
        ordering = ["min_lifetime_points"]

    def __str__(self) -> str:
        return f"{self.name} ({self.min_lifetime_points}+)"


class Achievement(models.Model):
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    points_bonus = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class CustomerAchievement(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="achievements")
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("customer", "achievement")

# Create your models here.
