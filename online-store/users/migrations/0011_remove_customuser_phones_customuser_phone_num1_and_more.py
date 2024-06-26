# Generated by Django 5.0.6 on 2024-05-24 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_createdat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phones',
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_num1',
            field=models.CharField(default='+998941633015', max_length=25),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_num2',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 6, 58, 58, 153209)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='zafarbekolimboyev07@gamil.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='passwordresetmodel',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 24, 6, 58, 58, 155103)),
        ),
    ]
