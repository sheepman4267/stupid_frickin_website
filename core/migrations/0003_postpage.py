# Generated by Django 5.1.2 on 2024-11-14 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_standardblockpage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPage',
            fields=[
                ('standardblockpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.standardblockpage')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.standardblockpage',),
        ),
    ]
