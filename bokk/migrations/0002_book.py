# Generated by Django 2.0.7 on 2018-07-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_id', models.IntegerField(default=0)),
                ('b_name', models.CharField(max_length=15)),
                ('b_auth', models.CharField(max_length=15)),
            ],
        ),
    ]
