from django.contrib import admin
from .models import User_data, Chat, BlockedUser
# Register your models here.
admin.site.register(User_data)
admin.site.register(Chat)
admin.site.register(BlockedUser)