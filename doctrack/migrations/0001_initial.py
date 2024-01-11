# Generated by Django 5.0.1 on 2024-01-11 06:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'label',
                'verbose_name_plural': 'labels',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=400)),
                ('file', models.FileField(upload_to='documents/')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctrack.document', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
        migrations.CreateModel(
            name='DocumentLabelRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Actor')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctrack.document')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctrack.label')),
            ],
            options={
                'verbose_name': 'documentlabel rel',
                'verbose_name_plural': 'documentlabel rels',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='labels',
            field=models.ManyToManyField(related_name='documents', through='doctrack.DocumentLabelRel', to='doctrack.label'),
        ),
    ]