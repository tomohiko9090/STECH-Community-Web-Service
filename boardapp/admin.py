from django.contrib import admin
from .models import BoardModel,Item, OrderItem, Order
# Register your models here.
admin.site.register(BoardModel)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)