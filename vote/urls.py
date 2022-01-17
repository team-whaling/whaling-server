from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

vote_router = DefaultRouter()
vote_router.register(r'votes', VoteViewSet, basename='vote')

choice_router = DefaultRouter()
choice_router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    path('', include(vote_router.urls)),
    path('', include(choice_router.urls))
]
