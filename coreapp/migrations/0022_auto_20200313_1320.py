# Generated by Django 3.0.4 on 2020-03-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0021_auto_20200313_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound',
            name='herb',
            field=models.ManyToManyField(to='coreapp.Herb'),
        ),
    ]