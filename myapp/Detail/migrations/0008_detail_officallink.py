# Generated by Django 4.1.5 on 2023-01-11 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Detail', '0007_detail_desgination'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='officalLink',
            field=models.CharField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
    ]
