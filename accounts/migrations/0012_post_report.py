# Generated by Django 2.2.6 on 2019-11-26 16:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0011_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='report',
            field=models.ManyToManyField(blank=True, related_name='report', to=settings.AUTH_USER_MODEL),
        ),
    ]