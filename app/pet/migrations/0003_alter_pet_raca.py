# Generated by Django 4.1.7 on 2023-05-19 11:43

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='raca',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='especie', chained_model_field='especie', on_delete=django.db.models.deletion.CASCADE, to='pet.raca'),
        ),
    ]