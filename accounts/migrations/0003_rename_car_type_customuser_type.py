# Generated by Django 4.1.4 on 2022-12-07 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_car_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='car_type',
            new_name='type',
        ),
    ]
