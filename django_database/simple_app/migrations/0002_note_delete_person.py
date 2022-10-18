# Generated by Django 4.1.2 on 2022-10-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now=True)),
                ('day_note', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]