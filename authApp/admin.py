from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.product import Products
from .models.categories import Categories

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Products)
admin.site.register(Categories)