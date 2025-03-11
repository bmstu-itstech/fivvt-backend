from django.contrib import admin

from albums.models import Album, Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
    )


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

    list_display = (
        'id',
        'title',
    )
