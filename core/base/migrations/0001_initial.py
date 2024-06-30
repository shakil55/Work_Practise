# Generated by Django 5.0.6 on 2024-06-13 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('pricing', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('link', models.URLField()),
                ('image', models.ImageField(upload_to='tool_images/')),
                ('tags', models.CharField(max_length=200)),
            ],
        ),
    ]
