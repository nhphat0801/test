# Generated by Django 3.0.4 on 2020-03-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0012_auto_20200312_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='compound',
            field=models.ManyToManyField(related_name='compound1', to='coreapp.Compound'),
        ),
    ]
