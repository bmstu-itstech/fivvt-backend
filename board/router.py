from rest_framework import viewsets

from board import models, serializers


class BoardViewSet(viewsets.ModelViewSet):
    queryset = models.MemberOfBoard.objects.all()
    serializer_class = serializers.MemberOfBoardSerializer
