# Generated by Django 3.2.8 on 2022-09-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220904_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='USERNAME_FIELD',
            field=models.CharField(max_length=10),
        ),
    ]
