# Generated by Django 4.1.5 on 2023-01-29 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Alltable", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order_number",
            fields=[
                (
                    "id",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Modle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField()),
                ("describe", models.CharField(max_length=800)),
                ("delivery_date", models.DateField()),
                ("logistics", models.IntegerField()),
                (
                    "order_number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="Alltable.order_number",
                    ),
                ),
            ],
        ),
    ]
