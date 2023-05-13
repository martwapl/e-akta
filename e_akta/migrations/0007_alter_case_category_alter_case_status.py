# Generated by Django 4.2 on 2023-05-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0006_alter_case_category_alter_case_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo karne', 'Prawo karne'), ('Prawo cywilne', 'Prawo cywilne'), ('Prawo rodzinne', 'Prawo rodzinne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Czeka na dekretację', 'Czeka na dekretację'), ('Zadekretowana', 'Zadekretowana'), ('Zarchiwizowana', 'Zarchiwizowana'), ('W toku', 'W toku'), ('Zakończona', 'Zakończona')]),
        ),
    ]