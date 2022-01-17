from django.db import models

from account.models import TimeStampedModel, User


class Vote(TimeStampedModel):
    # Enum class : IntegerChoices VS. TextChoices
    class StateOfVote(models.IntegerChoices):
        ONGOING = (1, '진행 중인 투표')
        FINISHED = (2, '완료된 투표')
        TRACKED = (3, '트래킹된 투표')

    class DurationOfQuestion(models.TextChoices):
        DAY = ('day', '1일 후')
        WEEK = ('week', '1주 후')
        MONTH = ('month', '1달 후')

    class CommentOfQuestion(models.TextChoices):
        UP = ('up', '올라갈까요')
        DOWN = ('down', '내려갈까요')

    # 다른 모델과의 관계
    vote_id = models.BigAutoField('투표 ID 번호', primary_key=True)
    uploader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='투표를 생성한 유저',
        related_name='created_votes',
        related_query_name='created_vote'
    )
    participants = models.ManyToManyField(
        User,
        verbose_name='투표에 참여한 유저들',
        related_name='participated_votes',
        related_query_name='participated_vote',
        through='Choice'
    )
    """
    아직 코인 서버 연결 X
    coin = models.ForeignKey(
        'Coin', 
        on_delete=models.CASCADE, 
        verbose_name='코인의 코드',
        related_name='',
        related_query_name=''
    )
    """

    # 투표 상태 정보
    state = models.IntegerField('투표 상태', choices=StateOfVote.choices, default=StateOfVote.ONGOING)
    finished_at = models.DateTimeField('투표가 종료되는 시점')
    tracked_at = models.DateTimeField('투표가 트래킹되는 시점')
    created_price = models.IntegerField('투표 생성 시점의 코인 가격')
    finished_price = models.IntegerField('투표 종료 시점의 코인 가격', null=True)
    spent_point = models.IntegerField('투표 참여 시 차감되는 고래밥', default=10)
    earned_point = models.IntegerField('정답 적중 시 지급되는 고래밥', default=20)
    is_answer = models.BooleanField('투표 결과 적중 여부', null=True)  # 전체 유저 투표 결과와 실제 가격 변동의 일치 여부

    # 투표 질문
    duration = models.CharField(
        '예상 기간',
        max_length=10,
        choices=DurationOfQuestion.choices,
    )
    range = models.IntegerField('예상 변동폭')
    comment = models.CharField(
        '예상 추이',
        max_length=10,
        choices=CommentOfQuestion.choices,
    )

    # 유저들의 투표 현황
    total_participants = models.IntegerField('투표 참가자 수', default=0)
    pos_participants = models.IntegerField('\'예\'를 선택한 유저 수', default=0)
    neg_participants = models.IntegerField('\'아니오\'를 선택한 유저 수', default=0)
    pos_whales = models.IntegerField('\'예\'를 선택한 웨일 수', default=0)
    neg_whales = models.IntegerField('\'아니오\'를 선택한 웨일 수', default=0)


class Choice(TimeStampedModel):
    class CaseOfChoice(models.IntegerChoices):
        YES = 1
        NO = 2

    choice_id = models.BigAutoField('투표 행위 ID', primary_key=True)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.IntegerField('유저의 선택', choices=CaseOfChoice.choices)
    is_answer = models.BooleanField('유저의 정답 여부', null=True)
