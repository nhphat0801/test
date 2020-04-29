# Generated by Django 3.0.4 on 2020-03-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0011_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='uniprot_ref',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='compound',
            field=models.ManyToManyField(related_name='compound', to='coreapp.Compound'),
        ),
    ]
