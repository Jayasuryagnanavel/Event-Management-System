# Generated by Django 3.0 on 2022-10-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20221007_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='meet_url',
            field=models.URLField(blank=True, max_length=2083, null=True),
        ),
    ]