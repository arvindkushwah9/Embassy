# Generated by Django 2.2.4 on 2019-12-09 10:40

from django.db import migrations, models
import esa_backend.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(storage=esa_backend.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]
