# Generated by Django 5.0 on 2024-02-18 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Event'),
        ),
    ]
