from django.contrib import admin

from hospitals.models import HospitalPhoto, Hospital, HospitalPhone


@admin.register(HospitalPhoto)
class HospitalPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
    )


class HospitalPhotoInline(admin.TabularInline):
    model = HospitalPhoto


class HospitalPhoneInline(admin.TabularInline):
    model = HospitalPhone


@admin.register(Hospital)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        HospitalPhoneInline,
        HospitalPhotoInline,
    ]

    list_display = (
        'id',
        'name',
        'address',
        'url',
        'url_on_map',
    )
