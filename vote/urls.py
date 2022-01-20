from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VoteViewSet

vote_router = DefaultRouter()
vote_router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('', include(vote_router.urls)),
]
