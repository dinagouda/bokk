# Generated by Django 2.0.7 on 2018-08-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokk', '0005_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artdesign',
            name='b_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='children',
            name='b_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='poetry',
            name='b_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='political',
            name='b_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='programing',
            name='b_name',
            field=models.CharField(max_length=40),
        ),
    ]
