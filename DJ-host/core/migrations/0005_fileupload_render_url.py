# Generated by Django 5.1.3 on 2024-11-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_fileupload_delete_file_uplode'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='render_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
