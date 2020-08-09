from django.contrib import admin
from .models import UserProfile, Orders

admin.site.register(Orders)
admin.site.register(UserProfile)
