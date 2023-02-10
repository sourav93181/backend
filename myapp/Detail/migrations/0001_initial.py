# Generated by Django 4.1.5 on 2023-01-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=250)),
                ('website', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=100)),
                ('jobType', models.CharField(max_length=13)),
                ('experience', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('Batch', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=13)),
                ('point1', models.CharField(max_length=250)),
                ('point2', models.CharField(max_length=250)),
                ('point3', models.CharField(max_length=250)),
                ('point4', models.CharField(max_length=250)),
                ('point5', models.CharField(max_length=250)),
            ],
        ),
    ]