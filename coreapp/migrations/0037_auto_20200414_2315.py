# Generated by Django 3.0.5 on 2020-04-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0036_auto_20200414_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compound',
            old_name='smiles',
            new_name='can_smiles',
        ),
        migrations.AddField(
            model_name='compound',
            name='iso_smiles',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='compound',
            field=models.ManyToManyField(to='coreapp.Compound'),
        ),
    ]
