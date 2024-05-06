# Generated by Django 5.0.4 on 2024-04-30 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_employeeprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dj_service_name', models.CharField(blank=True, max_length=250, null=True)),
                ('dj_service_description', models.CharField(blank=True, max_length=250, null=True)),
                ('dj_fully_booked', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'DJ Service',
                'verbose_name_plural': 'DJ Services',
            },
        ),
    ]