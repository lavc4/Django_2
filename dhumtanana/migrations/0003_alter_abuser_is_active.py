# Generated by Django 3.2.12 on 2022-02-22 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhumtanana', '0002_auto_20220222_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]