# Generated by Django 5.0.3 on 2024-03-25 13:02

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
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(verbose_name='description text')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('checked', models.BooleanField(default=False, verbose_name='checked')),
                ('date_start', models.DateTimeField(blank=True, default=None, null=True, verbose_name='date start')),
                ('date_end', models.DateTimeField(blank=True, default=None, null=True, verbose_name='date end')),
                ('date_time', models.DateTimeField(blank=True, default=None, null=True, verbose_name='date time')),
            ],
        ),
    ]