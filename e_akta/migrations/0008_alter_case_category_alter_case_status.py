# Generated by Django 4.2 on 2023-05-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0007_alter_case_category_alter_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo pracy', 'Prawo pracy'), ('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo cywilne', 'Prawo cywilne'), ('Prawo karne', 'Prawo karne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Czeka na dekretację', 'Czeka na dekretację'), ('W toku', 'W toku'), ('Zadekretowana', 'Zadekretowana'), ('Zakończona', 'Zakończona'), ('Zarchiwizowana', 'Zarchiwizowana')]),
        ),
    ]
