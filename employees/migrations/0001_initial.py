# Generated by Django 5.2 on 2025-04-10 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rank', models.PositiveIntegerField(help_text='Lower numbers are higher in the hierarchy (e.g., CEO=1)')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_joined', models.DateField()),
                ('last_promotion_date', models.DateField(blank=True, null=True)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('on_leave', 'On Leave'), ('terminated', 'Terminated')], max_length=50)),
                ('contact_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.contactinfo')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.role')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRoleHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_history', to='employees.employee')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.role')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
