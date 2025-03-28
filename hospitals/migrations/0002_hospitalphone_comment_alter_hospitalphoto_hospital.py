# Generated by Django 5.1.7 on 2025-03-16 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalphone',
            name='comment',
            field=models.CharField(help_text='Комментарий к номеру телефона, например, Справочная', max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='hospitalphoto',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='hospitals.hospital'),
        ),
    ]
