# Generated by Django 5.0 on 2023-12-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_alter_bildens_model_cellnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bildens_model',
            name='agree',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='Agree'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='agreeTerms',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='agree terms'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='authorize',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='Yes'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='cellNumber',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='cell number'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='codeArea',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='code area'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='codeCellArea',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='code cell area'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='employer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='gross',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='phoneNumber',
            field=models.IntegerField(blank=True, max_length=100, null=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='rent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='zipCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
