# Generated by Django 4.1.2 on 2022-10-09 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0003_keyboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('screen_resolution', models.CharField(max_length=100)),
                ('ports_and_types', models.JSONField()),
            ],
        ),
    ]