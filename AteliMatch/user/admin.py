from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
	model = User
	# Use the default UserAdmin configuration; customize list_display if desired
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
