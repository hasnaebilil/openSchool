# Generated by Django 2.1 on 2023-02-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rank', models.IntegerField()),
                ('description', models.CharField(max_length=2083)),
                ('video_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
