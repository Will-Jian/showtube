# Generated by Django 4.1.3 on 2022-11-23 00:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_post_options_remove_post_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 22, 18, 24, 11, 559090), verbose_name='Post Date'),
        ),
    ]