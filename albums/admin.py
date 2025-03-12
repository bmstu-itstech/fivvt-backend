from django.contrib import admin

from albums.models import Album, AlbumPhoto


@admin.register(AlbumPhoto)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
    )


class PhotoInline(admin.TabularInline):
    model = AlbumPhoto


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

    list_display = (
        'id',
        'title',
    )
