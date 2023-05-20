# Generated by Django 4.2 on 2023-05-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo karne', 'Prawo karne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo cywilne', 'Prawo cywilne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Zakończona', 'Zakończona'), ('W toku', 'W toku'), ('Zarchiwizowana', 'Zarchiwizowana')]),
        ),
    ]
