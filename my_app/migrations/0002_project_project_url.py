# Generated by Django 2.2.4 on 2020-04-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.URLField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]