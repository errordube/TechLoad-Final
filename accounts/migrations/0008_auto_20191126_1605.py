# Generated by Django 2.2.4 on 2019-11-26 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Likes',
        ),
        migrations.AddField(
            model_name='post',
            name='Likes',
            field=models.ManyToManyField(to='accounts.Like'),
        ),
    ]