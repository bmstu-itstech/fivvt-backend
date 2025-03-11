from rest_framework import serializers

from board.models import MemberOfBoard


class MemberOfBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberOfBoard
        fields = (
            'id',
            'full_name',
            'post',
            'biography',
            'image',
        )
