# Generated by Django 3.0 on 2022-10-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_auto_20221008_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='meet_url',
            field=models.URLField(blank=True, max_length=2083, null=True),
        ),
    ]
