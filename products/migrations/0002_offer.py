# Generated by Django 2.1 on 2020-05-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=7)),
                ('description', models.CharField(max_length=250)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
