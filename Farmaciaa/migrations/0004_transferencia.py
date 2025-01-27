# Generated by Django 5.1.5 on 2025-01-27 04:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmaciaa', '0003_remove_medicamento_cantidad_disponible_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Farmaciaa.medicamento')),
                ('sucursal_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencias_entrada', to='Farmaciaa.sucursal')),
                ('sucursal_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transferencias_salida', to='Farmaciaa.sucursal')),
            ],
        ),
    ]
