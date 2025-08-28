from django.contrib import admin
from .models import (
    RemittanceTransaction,
    PointsLedger,
    Tier,
    Achievement,
    CustomerAchievement,
)


@admin.register(RemittanceTransaction)
class RemittanceAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "amount_minor", "currency", "created_at")
    list_filter = ("currency",)
    search_fields = ("customer__full_name", "customer__phone_number")


@admin.register(PointsLedger)
class PointsLedgerAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "delta", "reason", "reference", "created_at")
    list_filter = ("reason",)
    search_fields = ("customer__full_name", "reference")


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ("name", "min_lifetime_points")
    list_editable = ("min_lifetime_points",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "points_bonus")
    search_fields = ("code", "name")


@admin.register(CustomerAchievement)
class CustomerAchievementAdmin(admin.ModelAdmin):
    list_display = ("customer", "achievement", "awarded_at")
    search_fields = ("customer__full_name", "achievement__code")

# Register your models here.
