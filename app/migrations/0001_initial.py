# Generated by Django 4.2.9 on 2024-01-22 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('roll_number', models.IntegerField(default=0, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
