# Generated by Django 3.1.13 on 2021-08-18 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cookies',
            options={'verbose_name': 'Cookies', 'verbose_name_plural': 'Cookies'},
        ),
        migrations.AlterModelOptions(
            name='privacy',
            options={'verbose_name': 'Privacy Policy', 'verbose_name_plural': 'Privacy Policies'},
        ),
    ]
