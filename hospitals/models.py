from django.db import models


class Hospital(models.Model):
    """
    Госпитали для ветеранов войны
    """
    name = models.CharField(
        max_length=100,
        help_text='Полное название госпиталя',
    )
    address = models.CharField(
        max_length=200,
        help_text='Подробный адрес до госпиталя',
    )
    url = models.URLField(
        blank=True,
        help_text='Опционально: ссылка на сайт госпиталя, если таковой есть',
    )
    url_on_map = models.URLField(
        help_text='Ссылка на местоположение госпиталя в Яндекс Картах, например, https://yandex.ru/maps/-/CHBl44Ny',
    )


class HospitalPhone(models.Model):
    """
    Телефон для связи с госпиталем для ветеранов
    """
    phone = models.CharField(
        primary_key=True,
        max_length=12,
        help_text='Телефон для связи с госпиталем в формате: +79999999999',
    )
    comment = models.CharField(
        blank=True,
        max_length=63,
        help_text='Комментарий к номеру телефона, например, Справочная',
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name = 'phones',
    )

    def __str__(self):
        return self.phone


class HospitalPhoto(models.Model):
    """
    Фотография госпиталя для ветеранов
    """
    image = models.ImageField(
        upload_to='photos/%Y/%m/%d',
        help_text='Фотография госпиталя с улицы для упрощения поиска',
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='photos',
    )

    def __str__(self):
        return self.image.name
