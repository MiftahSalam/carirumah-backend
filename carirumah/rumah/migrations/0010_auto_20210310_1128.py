# Generated by Django 3.1.7 on 2021-03-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rumah', '0009_auto_20210309_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]