# Generated by Django 2.0.7 on 2018-07-29 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=15)),
                ('L_name', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=15)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
    ]
