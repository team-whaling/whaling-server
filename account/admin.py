from django.contrib import admin

from account import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
