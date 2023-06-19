# Generated by Django 4.1.7 on 2023-06-08 21:04

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Especie",
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
                ("nome", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "especie",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Raca",
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
                ("nome", models.CharField(db_index=True, max_length=100, unique=True)),
                (
                    "especie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pet.especie"
                    ),
                ),
            ],
            options={
                "db_table": "raca",
            },
        ),
        migrations.CreateModel(
            name="Pet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("Macho", "Macho"), ("Fêmea", "Fêmea")], max_length=10
                    ),
                ),
                ("idade", models.IntegerField(default=0)),
                ("observacao", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "especie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="pet.especie"
                    ),
                ),
                (
                    "raca",
                    smart_selects.db_fields.ChainedForeignKey(
                        auto_choose=True,
                        chained_field="especie",
                        chained_model_field="especie",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pet.raca",
                    ),
                ),
            ],
            options={
                "db_table": "pet",
            },
        ),
    ]