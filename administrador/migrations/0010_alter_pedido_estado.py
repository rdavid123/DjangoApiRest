# Generated by Django 4.2.7 on 2023-11-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0009_alter_pedido_tipo_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('en camino', 'En camino'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=20),
        ),
    ]