from django.db import models


class MemberOfBoard(models.Model):
    """
    Член правления Фонда.
    """
    full_name = models.CharField(
        max_length=100,
        help_text='Полное имя члена правления Фонда, максимум 100 символов',
    )
    post = models.CharField(
        max_length=100,
        help_text='Должность члена правления Фонда, например, председатель',
    )
    biography = models.TextField(
        help_text='Краткая биография члена правления Фонда',
    )
    image = models.ImageField(
        upload_to='board/%Y/%m/%d',
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'member of board'
        verbose_name_plural = 'members of board'
