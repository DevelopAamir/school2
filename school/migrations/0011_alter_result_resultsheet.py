# Generated by Django 4.1.5 on 2023-03-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_alter_result_resultsheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='resultsheet',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
