# Generated by Django 4.0 on 2022-01-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice',
            field=models.IntegerField(choices=[(1, 'Yes'), (2, 'No')], verbose_name='유저의 선택'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='투표 행위 ID'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='state',
            field=models.IntegerField(choices=[(1, '진행 중인 투표'), (2, '완료된 투표'), (3, '트래킹된 투표')], default=1, verbose_name='투표 상태'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='투표 ID 번호'),
        ),
    ]