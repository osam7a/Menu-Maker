# Generated by Django 5.0.7 on 2024-07-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_thumbnail_remove_menu_thumbnail_menu_thumbnails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='thumbnails',
        ),
        migrations.AddField(
            model_name='menu',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text='The thumbnail image of the menu.', upload_to='static/uploads/'),
        ),
        migrations.DeleteModel(
            name='Thumbnail',
        ),
    ]
