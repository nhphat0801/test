# Generated by Django 3.0.4 on 2020-03-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0027_auto_20200318_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='compound',
            field=models.ManyToManyField(to='coreapp.Compound'),
        ),
    ]
