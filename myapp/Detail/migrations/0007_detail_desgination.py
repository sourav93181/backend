# Generated by Django 4.1.5 on 2023-01-11 10:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Detail', '0006_detail_companydescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='desgination',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
