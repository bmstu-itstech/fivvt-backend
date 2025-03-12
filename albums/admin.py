from django.contrib import admin

from albums.models import Album, AlbumPhoto, AlbumMainPhoto


class AlbumPhotoInline(admin.TabularInline):
    model = AlbumPhoto


class AlbumMainPhotoInline(admin.TabularInline):
    model = AlbumMainPhoto


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        AlbumPhotoInline,
        AlbumMainPhotoInline,
    ]

    list_display = (
        'id',
        'title',
    )
