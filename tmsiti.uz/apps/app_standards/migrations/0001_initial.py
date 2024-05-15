# Generated by Django 5.0.4 on 2024-05-08 13:42

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
            name='StandardTypesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_type', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'StandardsTypes',
                'db_table': 'StandardsTypes',
            },
        ),
        migrations.CreateModel(
            name='StandardsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_code', models.CharField(max_length=55)),
                ('standard_description', models.CharField(max_length=255)),
                ('standard_text', models.TextField(null=True)),
                ('standard_file', models.FileField(null=True, upload_to='Standards/%y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('standard_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_standards.standardtypesmodel')),
            ],
            options={
                'verbose_name_plural': 'standards',
                'db_table': 'standards',
            },
        ),
    ]
