# Generated by Django 3.0.6 on 2021-05-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_user', '0007_auto_20210529_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentsmodel',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='commentsmodel',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]