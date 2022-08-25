# Generated by Django 3.2 on 2022-08-25 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('salary', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=120, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeapp.department')),
            ],
        ),
    ]
