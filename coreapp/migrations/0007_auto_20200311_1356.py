# Generated by Django 3.0.4 on 2020-03-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0006_auto_20200311_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='herb',
            name='flower',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='fruit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='image0',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='image1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='image2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='image3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='image_ref',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='leaf',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='root',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='stem',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='herb',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]