# Generated by Django 4.2.6 on 2023-10-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=40)),
                ('about', models.CharField(max_length=40)),
                ('deadline', models.DateField()),
                ('done', models.BooleanField()),
            ],
        ),
    ]
