# Generated by Django 5.1.5 on 2025-01-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
