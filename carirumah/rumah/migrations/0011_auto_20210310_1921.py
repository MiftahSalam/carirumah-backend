# Generated by Django 3.1.7 on 2021-03-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rumah', '0010_auto_20210310_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
