# Generated by Django 2.2.2 on 2019-06-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20190328_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='index', max_length=50, verbose_name='Kategori'),
        ),
    ]
