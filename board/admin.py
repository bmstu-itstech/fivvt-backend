from django.contrib import admin

from board.models import MemberOfBoard


@admin.register(MemberOfBoard)
class MemberOfBoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'post',
        'biography',
        'image',
    )
