# Generated by Django 5.0.4 on 2024-05-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_standards', '0002_standardsmodel_standard_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardsmodel',
            name='standard_year',
            field=models.CharField(max_length=15),
        ),
    ]
