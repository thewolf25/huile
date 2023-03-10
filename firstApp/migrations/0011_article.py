# Generated by Django 4.1.3 on 2022-12-02 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0010_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('status', models.CharField(choices=[(1, 'Vaidé'), (2, 'En Attente'), (3, 'Refusée')], max_length=100)),
                ('qte', models.IntegerField()),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firstApp.type')),
            ],
        ),
    ]
