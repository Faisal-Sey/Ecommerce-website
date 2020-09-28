from django.contrib import admin
from .models import UserDb, item, Shoes, OrderItem, Order, BillingAddress, ShopMain, LatestProductOne, LatestProduct, \
    TopProductOne, TopProduct, ReviewProduct, ReviewProductOne, Watches, Shirts, Shorts, Pants, Slippers,Post
# Register your models here.

admin.site.register(UserDb)
admin.site.register(item)
admin.site.register(Shoes)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingAddress)
admin.site.register(ShopMain)
admin.site.register(LatestProductOne)
admin.site.register(LatestProduct)
admin.site.register(TopProductOne)
admin.site.register(TopProduct)
admin.site.register(ReviewProduct)
admin.site.register(ReviewProductOne)
admin.site.register(Watches)
admin.site.register(Shirts)
admin.site.register(Shorts)
admin.site.register(Slippers)
admin.site.register(Pants)
admin.site.register(Post)