from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone_number", "country", "date_joined")
    search_fields = ("full_name", "phone_number", "user__username")
    list_filter = ("country",)

# Register your models here.
