# Generated by Django 3.1.1 on 2020-09-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20200926_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
