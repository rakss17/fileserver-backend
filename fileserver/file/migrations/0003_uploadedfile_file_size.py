# Generated by Django 4.2.6 on 2023-11-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_uploadedfile_original_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='file_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]