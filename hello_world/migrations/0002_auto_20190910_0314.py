# Generated by Django 2.2.3 on 2019-09-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/Users/msdaram/venv/portfolio/hello_world/static'),
        ),
    ]