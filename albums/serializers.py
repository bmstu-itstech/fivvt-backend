from rest_framework import serializers

from albums.models import Album, AlbumPhoto, AlbumMainPhoto


class AlbumPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPhoto
        fields = (
            'id',
            'image',
            'uploaded_at',
        )


class AlbumMainPhotoSerializer(serializers.ModelSerializer):
    photo = AlbumPhotoSerializer(read_only=True)

    class Meta:
        model = AlbumMainPhoto
        fields = (
            'photo',
        )


class AlbumSerializer(serializers.ModelSerializer):
    photos = AlbumPhotoSerializer(many=True)
    main_photo = AlbumMainPhotoSerializer()

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'photos',
            'main_photo',
            'created_at',
        )
