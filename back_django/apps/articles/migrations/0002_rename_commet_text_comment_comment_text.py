# Generated by Django 5.0.3 on 2024-03-21 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commet_text',
            new_name='comment_text',
        ),
    ]