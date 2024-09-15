from django.contrib import admin

from apps.models import Packages, Contacts, Booking
from django.contrib import admin
from .models import ClickTransaction


# Register your models here.
@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass


@admin.register(ClickTransaction)
class ClickTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "click_paydoc_id",
        "amount",
        "status",
    )
    list_display_links = ("id", "amount")
    list_filter = ("status",)
    search_fields = ["status", "id", "click_paydoc_id"]
    save_on_top = True
