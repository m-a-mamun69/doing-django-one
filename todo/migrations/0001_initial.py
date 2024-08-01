# Generated by Django 5.0.7 on 2024-08-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=85)),
                ('content', models.CharField(max_length=300)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
