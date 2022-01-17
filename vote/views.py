from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import VoteCreateSerializer, VoteListSerializer, ChoiceSerializer
from .models import Vote, Choice


class VoteViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return Vote.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VoteListSerializer(queryset, many=True)
        for data in serializer.data:
            participants = data.pop('participants')
            if request.user.user_id in participants:
                voted = True
            else:
                voted = False
            data['voted'] = voted
        return Response(serializer.data)


# class VoteModelViewSet(viewsets.ModelViewSet):
#     serializer_class = VoteCreateSerializer
#     queryset = Vote.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
