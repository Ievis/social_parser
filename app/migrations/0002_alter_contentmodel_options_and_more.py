# Generated by Django 5.0.7 on 2024-08-05 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contentmodel',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='highlightmodel',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='highlightmodel',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 10, 15, 44, 972862, tzinfo=datetime.timezone.utc), verbose_name='published at'),
        ),
        migrations.AlterField(
            model_name='contentmodel',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 5, 10, 15, 44, 971960, tzinfo=datetime.timezone.utc), verbose_name='published at'),
        ),
    ]
