from django.contrib import admin

from vote import models


@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['vote_id', 'coin', 'state', 'duration', 'range', 'comment', 'created_price', 'finished_price',
                    'finished_at',
                    'tracked_at', 'is_answer']
    list_display_links = ['vote_id', 'state', 'created_price', 'finished_price', 'finished_at', 'tracked_at']


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['participant', 'choice', 'is_answer']
    list_display_links = ['choice']


@admin.register(models.Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['code', 'krname', 'name', 'image']
    list_display_links = ['code', 'krname', 'name', 'image']
