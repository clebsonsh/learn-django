# Generated by Django 5.0.7 on 2024-07-27 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='pub_at',
        ),
    ]
