from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vote.views import VoteViewSet, acc_percent_of_whaling, CoinViewSet

vote_router = DefaultRouter()
vote_router.register(r'votes', VoteViewSet)
vote_router.register(r'coins', CoinViewSet)
urlpatterns = [
    # 웨일링 적중률
    path('acc-percent', acc_percent_of_whaling),
    # 투표
    path('', include(vote_router.urls))
]
