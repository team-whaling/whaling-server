# Generated by Django 4.0 on 2022-01-15 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_alter_user_nickname_alter_user_user_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('choice_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='투표 행위 ID')),
                ('choice', models.BooleanField(verbose_name='유저의 선택')),
                ('is_answer', models.BooleanField(null=True, verbose_name='유저의 정답 여부')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vote_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='투표 ID 번호')),
                ('state', models.IntegerField(choices=[(0, '진행 중인 투표'), (1, '완료된 투표'), (2, '트래킹된 투표')], default=0, verbose_name='투표 상태')),
                ('finished_at', models.DateTimeField(verbose_name='투표가 종료되는 시점')),
                ('tracked_at', models.DateTimeField(verbose_name='투표가 트래킹되는 시점')),
                ('created_price', models.IntegerField(verbose_name='투표 생성 시점의 코인 가격')),
                ('finished_price', models.IntegerField(null=True, verbose_name='투표 종료 시점의 코인 가격')),
                ('spent_point', models.IntegerField(default=10, verbose_name='투표 참여 시 차감되는 고래밥')),
                ('earned_point', models.IntegerField(default=20, verbose_name='정답 적중 시 지급되는 고래밥')),
                ('is_answer', models.BooleanField(null=True, verbose_name='투표 결과 적중 여부')),
                ('is_admin_vote', models.BooleanField(default=False, verbose_name='운영자 투표 여부')),
                ('duration', models.CharField(choices=[('day', '1일 후'), ('week', '1주 후'), ('month', '1달 후')], max_length=10, verbose_name='예상 기간')),
                ('range', models.IntegerField(verbose_name='예상 변동폭')),
                ('comment', models.CharField(choices=[('up', '올라갈까요'), ('down', '내려갈까요')], max_length=10, verbose_name='예상 추이')),
                ('pos_participants', models.IntegerField(default=0, verbose_name="'예'를 선택한 유저 수")),
                ('neg_participants', models.IntegerField(default=0, verbose_name="'아니오'를 선택한 유저 수")),
                ('pos_whales', models.IntegerField(default=0, verbose_name="'예'를 선택한 웨일 수")),
                ('neg_whales', models.IntegerField(default=0, verbose_name="'아니오'를 선택한 웨일 수")),
                ('participants', models.ManyToManyField(related_name='participated_votes', related_query_name='participated_vote', through='vote.Choice', to=settings.AUTH_USER_MODEL, verbose_name='투표에 참여한 유저들')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_votes', related_query_name='created_vote', to='account.user', verbose_name='투표를 생성한 유저')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.vote'),
        ),
    ]