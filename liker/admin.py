from django.contrib import admin
from .models import *


class UserDataAdmin(admin.ModelAdmin):
	list_display = ['login', 'password',]

	class Meta:
		model = UserData

admin.site.register(UserData, UserDataAdmin)
