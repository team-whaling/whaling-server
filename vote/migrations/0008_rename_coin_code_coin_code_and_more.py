# Generated by Django 4.0 on 2022-01-19 11:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('vote', '0007_vote_coin_alter_choice_choice'),
    ]
    operations = [
        migrations.RenameField(
            model_name='coin',
            old_name='coin_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='coin',
            old_name='coin_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='coin',
            old_name='coin_krname',
            new_name='krname',
        ),
        migrations.RenameField(
            model_name='coin',
            old_name='coin_name',
            new_name='name',
        ),
    ]
