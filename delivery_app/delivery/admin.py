from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Customer, AdminUser, Shipper, User, Discount, Order, Post, Auction


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff', 'is_active', 'is_admin', 'is_customer', 'is_shipper']
    list_filter = ['id', 'date_joined', 'is_active']
    search_fields = ['username']


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


class AdminUserAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


class ShipperAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar']

    def avatar(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />' \
                    .format(url=obj.image.name)
            )


admin.site.site_header = "Delivery Manager System"
admin.site.site_title = "Delivery Admin"
admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(Shipper, ShipperAdmin)
