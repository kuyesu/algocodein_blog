# Generated by Django 3.1.13 on 2021-08-23 09:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailstreamforms.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailstreamforms', '0002_form_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('form', wagtail.core.blocks.StructBlock([('form', wagtailstreamforms.blocks.FormChooserBlock()), ('form_action', wagtail.core.blocks.CharBlock(help_text='The form post action. "" or "." for the current page or a url', required=False)), ('form_reference', wagtailstreamforms.blocks.InfoBlock(help_text='This form will be given a unique reference once saved', required=False))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='AdvancedFormSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_address', models.EmailField(max_length=254)),
                ('form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advanced_settings', to='wagtailstreamforms.form')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
