# Generated by Django 2.2.2 on 2019-06-15 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_category_slug2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categoriess'},
        ),
    ]