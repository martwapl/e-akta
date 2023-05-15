# Generated by Django 4.2 on 2023-05-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo cywilne', 'Prawo cywilne'), ('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo karne', 'Prawo karne')], default='Prawo karne'),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Zakończona', 'Zakończona'), ('Zarchiwizowana', 'Zarchiwizowana'), ('W toku', 'W toku')]),
        ),
    ]
