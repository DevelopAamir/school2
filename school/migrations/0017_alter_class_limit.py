# Generated by Django 4.1.5 on 2023-03-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_class_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='limit',
            field=models.IntegerField(default=50),
        ),
    ]
