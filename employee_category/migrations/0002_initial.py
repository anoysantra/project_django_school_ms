# Generated by Django 4.2.5 on 2023-10-04 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('category_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
    ]
