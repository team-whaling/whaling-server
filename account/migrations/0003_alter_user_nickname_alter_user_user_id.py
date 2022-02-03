# Generated by Django 4.0 on 2022-01-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, unique=True, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.BigIntegerField(primary_key=True, serialize=False, verbose_name='회원번호'),
        ),
    ]
