# Generated by Django 4.2.1 on 2023-06-08 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_breed_bug_subject_remove_bug_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='age',
        ),
        migrations.AddField(
            model_name='bug',
            name='language',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]