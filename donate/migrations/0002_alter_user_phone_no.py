# Generated by Django 4.2.1 on 2023-06-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
