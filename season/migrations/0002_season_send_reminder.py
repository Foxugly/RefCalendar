# Generated by Django 4.0.2 on 2022-02-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='send_reminder',
            field=models.BooleanField(default=False),
        ),
    ]