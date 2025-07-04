# Generated by Django 5.2.3 on 2025-06-28 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street1_address', models.CharField(max_length=255)),
                ('street2_address', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='staffbase',
            name='address',
        ),
        migrations.AddField(
            model_name='intern',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intern_address', to='employees.address'),
        ),
        migrations.AddField(
            model_name='manager',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_address', to='employees.address'),
        ),
    ]
