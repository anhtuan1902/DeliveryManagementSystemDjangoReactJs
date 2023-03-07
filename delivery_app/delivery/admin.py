from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Customer, AdminUser, Shipper, Discount, Order, Post, Auction


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    list_display = ['avatar', 'username', 'email', 'first_name', 'last_name', 'CMND', 'already_verify', 'is_active',
                    'created_date']


admin.site.site_header = "Delivery Manager System"
admin.site.site_title = "Delivery Admin"
admin.site.register(Customer)
admin.site.register(AdminUser)
