# Generated by Django 3.0.6 on 2021-01-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
    ]
