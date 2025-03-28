# Generated by Django 5.1.4 on 2025-01-12 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_description', models.CharField(max_length=255)),
                ('duration', models.FloatField()),
                ('price', models.FloatField()),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='account_module.stylist')),
            ],
        ),
        migrations.CreateModel(
            name='Tokenism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokenism', to='stylist.services')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('tokenism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='stylist.tokenism')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_recurring', models.BooleanField(default=False)),
                ('day_of_week', models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True)),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='account_module.stylist')),
            ],
            options={
                'ordering': ['date', 'start_time'],
                'unique_together': {('stylist', 'date', 'start_time', 'end_time')},
            },
        ),
    ]
