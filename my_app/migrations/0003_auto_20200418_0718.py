# Generated by Django 2.2.4 on 2020-04-18 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_project_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_url',
            field=models.CharField(max_length=2083),
        ),
    ]