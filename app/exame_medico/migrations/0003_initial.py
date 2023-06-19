# Generated by Django 4.1.7 on 2023-06-08 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("exame_medico", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="examemedico",
            name="veterinario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="users.veterinario"
            ),
        ),
    ]