# Generated by Django 4.2 on 2023-05-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo cywilne', 'Prawo cywilne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo karne', 'Prawo karne'), ('Prawo rodzinne', 'Prawo rodzinne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Czeka na dekretację', 'Czeka na dekretację'), ('Zadekretowana', 'Zadekretowana'), ('W toku', 'W toku'), ('Zarchiwizowana', 'Zarchiwizowana'), ('Zakończona', 'Zakończona')]),
        ),
    ]
