# Generated by Django 4.0.6 on 2025-03-09 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0060_wsd'),
    ]

    operations = [
        migrations.CreateModel(
            name='ET0ExecutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
            ],
        ),
    ]
