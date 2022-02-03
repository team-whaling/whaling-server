from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vote.views import VoteViewSet, acc_percent_of_whaling, CoinViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'votes', VoteViewSet)
router.register(r'coins', CoinViewSet)
router_with_slash = DefaultRouter(trailing_slash=True)
router_with_slash.register(r'votes', VoteViewSet)
router_with_slash.register(r'coins', CoinViewSet)

urlpatterns = [
    # 웨일링 적중률
    path('acc-percent', acc_percent_of_whaling),
    # 투표 및 코인
    path('', include(router.urls)),
    path('', include(router_with_slash.urls)),
]
