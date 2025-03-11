from django import forms

from board.models import MemberOfBoard


class MemberOfBoardAdminForm(forms.ModelForm):
    class Meta:
        model = MemberOfBoard
        fields = (
            'full_name',
            'post',
            'biography',
            'image',
        )
        widgets = {
            'full_name': forms.TextInput,
            'post':      forms.TextInput,
            'biography': forms.TextInput,
            'image':     forms.FileInput,
        }
