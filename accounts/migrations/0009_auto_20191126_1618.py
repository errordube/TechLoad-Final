# Generated by Django 2.2.4 on 2019-11-26 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20191126_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
