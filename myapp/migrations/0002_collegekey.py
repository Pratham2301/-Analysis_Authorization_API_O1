# Generated by Django 4.0.1 on 2022-05-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=500)),
                ('key', models.CharField(max_length=500, unique=True)),
            ],
        ),
    ]
