# Generated by Django 2.2.2 on 2019-06-12 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]