# Generated by Django 3.1.7 on 2021-03-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rumah', '0005_auto_20210308_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rumah',
            name='status',
            field=models.CharField(choices=[('JL', 'Jual'), ('SW', 'Sewa'), ('JS', 'Jual/Sewa')], max_length=2),
        ),
    ]
