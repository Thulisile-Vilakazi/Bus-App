from django.contrib import admin
from .models import Reward, Redemption, RedemptionItem


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "category", "points_cost", "stock", "active")
    list_filter = ("category", "active")
    search_fields = ("sku", "name")


class RedemptionItemInline(admin.TabularInline):
    model = RedemptionItem
    extra = 0


@admin.register(Redemption)
class RedemptionAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "total_points", "status", "created_at")
    list_filter = ("status",)
    inlines = [RedemptionItemInline]

# Register your models here.
