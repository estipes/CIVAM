# Generated by Django 2.2.6 on 2020-05-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civam', '0002_auto_20200528_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personorinstitute',
            name='dates',
        ),
        migrations.AddField(
            model_name='personorinstitute',
            name='private_catalog_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personorinstitute',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personorinstitute',
            name='historical_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personorinstitute',
            name='private_notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
