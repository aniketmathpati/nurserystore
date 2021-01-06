# Generated by Django 3.0.6 on 2021-01-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('nurseryId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('nurseryName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'Nursery',
            },
        ),
    ]