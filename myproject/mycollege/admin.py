from django.contrib import admin
from .models import CanteenItem, MessItem, BakeryItem

admin.site.register(CanteenItem)
admin.site.register(MessItem)
admin.site.register(BakeryItem)
class CanteenItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
