# Generated by Django 3.0 on 2022-10-07 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20221008_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
    ]
