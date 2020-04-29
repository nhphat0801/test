# Generated by Django 3.0.4 on 2020-03-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0032_auto_20200318_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='compound',
            field=models.ManyToManyField(to='coreapp.Compound'),
        ),
        migrations.AlterField(
            model_name='target',
            name='protein_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
