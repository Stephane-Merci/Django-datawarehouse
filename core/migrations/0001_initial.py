# Generated by Django 5.0 on 2024-01-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alcohol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('town', models.TextField(max_length=100)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('item_type', models.CharField(max_length=100)),
                ('warehouse_sales', models.FloatField(max_length=100)),
            ],
        ),
    ]
