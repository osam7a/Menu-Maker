# Generated by Django 5.0.7 on 2024-07-19 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_category_title_bg_remove_category_title_bn_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='languages',
            new_name='languages_allowed',
        ),
    ]