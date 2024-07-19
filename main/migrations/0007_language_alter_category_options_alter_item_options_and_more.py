# Generated by Django 5.0.7 on 2024-07-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_menu_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menus'},
        ),
        migrations.AddField(
            model_name='category',
            name='title_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_bg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_bn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_cs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_da',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_el',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_et',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_fi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_hi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_hr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_hu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ind',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_is',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_it',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_lo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_lt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_lv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_nl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_pa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_pl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_sk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_sl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_sr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_sv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_tr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_uk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_zh',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_bg',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_bn',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_cs',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_da',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_el',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_et',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_fa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_fi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_hi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_hr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_hu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ind',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_is',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_it',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ja',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ko',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_lo',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_lt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_lv',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_nl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_no',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_pa',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_pl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_pt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_sk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_sl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_sr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_sv',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_th',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_ur',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_vi',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients_zh',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_bg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_bn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_cs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_da',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_el',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_et',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_fi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_hi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_hr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_hu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ind',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_is',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_it',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_lo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_lt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_lv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_nl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_pa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_pl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_sk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_sl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_sr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_sv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_tr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_uk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_ur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='title_zh',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_bg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_bn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_cs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_da',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_el',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_et',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_fi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_hi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_hr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_hu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ind',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_is',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_it',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_lo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_lt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_lv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_nl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_pa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_pl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_sk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_sl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_sr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_sv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_tr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_uk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_ur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='address_zh',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_bg',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_bn',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_cs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_da',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_el',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_et',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_fa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_fi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_hi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_hr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_hu',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ind',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_is',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_it',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_lo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_lt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_lv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_nl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_pa',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_pl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ro',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_sk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_sl',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_sr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_sv',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_tr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_uk',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_ur',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_zh',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='languages',
            field=models.ManyToManyField(to='main.language'),
        ),
    ]
