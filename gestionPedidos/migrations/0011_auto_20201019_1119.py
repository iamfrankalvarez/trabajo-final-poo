# Generated by Django 3.1.2 on 2020-10-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0010_auto_20201017_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='earnings',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='sales',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='products',
            name='update_date',
            field=models.BigIntegerField(default=0),
        ),
    ]
