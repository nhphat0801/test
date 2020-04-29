# Generated by Django 3.0.4 on 2020-03-12 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0013_auto_20200312_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='target',
            name='herb',
        ),
        migrations.AlterField(
            model_name='target',
            name='compound',
            field=models.ManyToManyField(related_name='compound', to='coreapp.Compound'),
        ),
    ]