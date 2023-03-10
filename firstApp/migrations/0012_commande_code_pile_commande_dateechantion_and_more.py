# Generated by Django 4.1.3 on 2022-12-04 12:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
import firstApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0011_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='code_pile',
            field=models.CharField(default='rs 400', max_length=100),
        ),
        migrations.AddField(
            model_name='commande',
            name='dateEchantion',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 12, 4, 13, 17, 7, 110457)),
        ),
        migrations.AddField(
            model_name='commande',
            name='gouvernorat',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='firstApp.gouvernorat'),
        ),
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(default='202212041317078', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='qte',
            field=models.IntegerField(validators=[firstApp.models.postiveValueValidator]),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('validé', 'Vaidé'), ('en attente', 'En Attente'), ('refusée', 'Refusée')], max_length=100),
        ),
    ]
