# Generated by Django 2.2.6 on 2020-05-24 16:04

import civam.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/')),
                ('public', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='collections_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cover_image', models.ImageField(blank=True, upload_to='cover_images/items/')),
                ('description', models.TextField(blank=True)),
                ('culture_or_community', models.CharField(blank=True, max_length=127, null=True)),
                ('heritage_type', models.CharField(blank=True, max_length=127, null=True)),
                ('date_of_creation', models.DateTimeField(blank=True, null=True)),
                ('physical_details', models.CharField(blank=True, max_length=255, null=True)),
                ('reproduction_rights', models.CharField(blank=True, max_length=127, null=True)),
                ('place_created', models.CharField(blank=True, max_length=127, null=True)),
                ('source', models.CharField(blank=True, max_length=127, null=True)),
                ('accession_number', models.CharField(blank=True, max_length=31, null=True)),
                ('accession_date', models.DateTimeField(blank=True, null=True)),
                ('external_link', models.URLField(blank=True, null=True)),
                ('provenance', models.CharField(blank=True, max_length=127, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='civam.Collection')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnails/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='civam.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stories_created', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='civam.Item')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stories_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.CreateModel(
            name='PorI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=125)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PorI_created', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Pori_modified', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=31)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='civam.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPorI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='civam.Item')),
                ('pori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='civam.PorI')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(upload_to=civam.models.image_upload_path)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='civam.Item')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('default', models.BooleanField(default=False)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='civam.Collection')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='auth.Group')),
            ],
            options={
                'unique_together': {('name', 'collection')},
            },
        ),
    ]
