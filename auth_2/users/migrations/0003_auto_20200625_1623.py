# Generated by Django 3.0.7 on 2020-06-25 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200625_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='email'),
        ),
    ]
