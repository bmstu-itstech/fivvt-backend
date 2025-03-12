from django.db import models


class Album(models.Model):
    """
    Альбом с фотографиями с мероприятий.
    """
    title = models.CharField(
        max_length=100,
        help_text='Название альбом, обычно совпадает с названием мероприятия, например: Мероприятие, посвященное 20-летию создания РРОФИВА'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title


class AlbumPhoto(models.Model):
    """
    Фотография в альбоме.
    """
    image = models.ImageField(
        upload_to='albums/%Y/%m/%d',
    )
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
    album = models.ForeignKey(
        Album,
        related_name='photos',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.image.url


class AlbumMainPhoto(models.Model):
    """
    Заглавная фотография альбома, которая будет на обложке.
    """
    album = models.OneToOneField(Album, related_name='main_photo', on_delete=models.CASCADE)
    photo = models.ForeignKey(AlbumPhoto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.photo)
