# Generated by Django 3.1.13 on 2021-08-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='title_ar_ae',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='title_sw_ke',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_ar_ae',
            field=models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_en',
            field=models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_es',
            field=models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_fr',
            field=models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title_sw_ke',
            field=models.CharField(help_text='Title of menu item that will be displayed', max_length=50, null=True),
        ),
    ]
