from django.contrib import admin

from vote import models


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
