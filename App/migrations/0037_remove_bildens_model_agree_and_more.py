# Generated by Django 5.0 on 2023-12-23 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0036_alter_bildens_model_agree_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bildens_model',
            name='agree',
        ),
        migrations.RemoveField(
            model_name='bildens_model',
            name='agreeTerms',
        ),
        migrations.RemoveField(
            model_name='bildens_model',
            name='authorize',
        ),
        migrations.RemoveField(
            model_name='bildens_model',
            name='married',
        ),
        migrations.RemoveField(
            model_name='bildens_model',
            name='other',
        ),
        migrations.RemoveField(
            model_name='bildens_model',
            name='single',
        ),
    ]
