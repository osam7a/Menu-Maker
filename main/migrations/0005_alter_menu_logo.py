# Generated by Django 5.0.4 on 2024-07-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_menu_resturaunt_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='logo',
            field=models.ImageField(upload_to='static/uploads/'),
        ),
    ]
