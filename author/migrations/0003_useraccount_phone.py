# Generated by Django 4.2.7 on 2024-01-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_useraccount_coin_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
