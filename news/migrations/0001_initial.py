# Generated by Django 2.2 on 2019-05-26 07:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('update_date', models.DateTimeField(verbose_name='date updated')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='id+', to=settings.AUTH_USER_MODEL)),
                ('updater', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='id+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
