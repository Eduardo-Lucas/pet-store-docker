# Generated by Django 4.1.7 on 2023-06-17 14:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("exame_medico", "0004_delete_examemedico_delete_tipoexame"),
        ("pet", "0003_remove_pet_especie_remove_pet_raca_remove_pet_tutor_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_permissions",
        ),
        migrations.DeleteModel(
            name="Veterinario",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
