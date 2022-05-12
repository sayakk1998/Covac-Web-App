# Generated by Django 3.2.3 on 2021-07-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=12)),
                ('vaccinecenter', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=10)),
                ('idnumber', models.CharField(max_length=20)),
                ('appointment', models.CharField(max_length=10)),
                ('dose', models.CharField(max_length=10)),
                ('date', models.DateField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
    ]