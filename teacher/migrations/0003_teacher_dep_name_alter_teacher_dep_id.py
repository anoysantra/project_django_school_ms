# Generated by Django 4.2.5 on 2023-10-04 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20231005_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='dep_name',
            field=models.CharField(default='Physics', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='dep_id',
            field=models.CharField(max_length=10),
        ),
    ]