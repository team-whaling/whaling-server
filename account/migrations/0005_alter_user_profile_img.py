# Generated by Django 4.0.1 on 2022-01-30 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_created_at_alter_user_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.URLField(blank=True, null=True, verbose_name='프로필 url'),
        ),
    ]