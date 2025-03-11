from django.db import models


class MemberOfBoard(models.Model):
    """
    Член правления Фонда.
    """

    id = models.BigAutoField(
        primary_key=True,
        serialize=False,
    )
    full_name = models.CharField(
        max_length=100,
        help_text='Полное имя члена правления Фонда, максимум 100 символов',
    )
    post = models.CharField(
        max_length=100,
        help_text='Должность члена правления Фонда, например, Председатель',
    )
    biography = models.TextField(
        help_text='Краткая биография члена правления Фонда',
    )
    image = models.ImageField(
        upload_to='board',
    )

    class Meta:
        verbose_name = 'member of board'
        verbose_name_plural = 'members of board'
