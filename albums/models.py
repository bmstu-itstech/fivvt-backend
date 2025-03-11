from django.db import models


class Album(models.Model):
    """
    Альбом с фотографиями с мероприятий.
    """

    id = models.BigAutoField(
        primary_key=True,
        serialize=False,
    )
    title = models.CharField(
        max_length=100,
        help_text='Название альбом, обычно совпадает с названием мероприятия, например: Мероприятие, посвященное 20-летию создания РРОФИВА'
    )

    def __str__(self):
        return self.title


class Photo(models.Model):
    """
    Фотография в альбоме.
    """

    id = models.BigAutoField(
        primary_key=True,
        serialize=False,
    )
    image = models.ImageField(
        upload_to='albums/%Y/%m/%d',
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='photos',
    )

    def __str__(self):
        return self.image.url
