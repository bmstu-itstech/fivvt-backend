from rest_framework import serializers

from albums.models import Album, AlbumPhoto


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = (
            'id',
            'image',
        )


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True)

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'photos',
        )
