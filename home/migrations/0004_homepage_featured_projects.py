# Generated by Django 5.1.2 on 2024-11-14 04:05

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featured_projects',
            field=wagtail.fields.StreamField([('featured_project', 1)], blank=True, block_lookup={0: ('wagtail.blocks.PageChooserBlock', (), {}), 1: ('wagtail.blocks.StructBlock', [[('featured_page', 0)]], {})}, null=True),
        ),
    ]
