# Generated by Django 5.0.1 on 2024-03-17 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_alter_inventory_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tiles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='position',
            field=models.JSONField(default=dict),
        ),
    ]