# Generated by Django 4.1.2 on 2022-10-09 21:09

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0004_monitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='ports_and_types',
        ),
        migrations.AddField(
            model_name='monitor',
            name='port_types',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('1', 'vga'), ('2', 'hdmi'), ('3', 'optical')], default='hdmi', max_length=20),
            preserve_default=False,
        ),
    ]
