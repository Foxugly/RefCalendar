# Generated by Django 4.0.2 on 2022-02-15 14:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('season', '0003_season_content_email_season_title_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='content_email',
            field=ckeditor.fields.RichTextField(default='content email', verbose_name='content email'),
        ),
    ]
