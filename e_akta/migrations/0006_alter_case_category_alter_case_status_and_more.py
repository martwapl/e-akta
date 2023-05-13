# Generated by Django 4.2 on 2023-05-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0005_alter_case_category_alter_case_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo cywilne', 'Prawo cywilne'), ('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo karne', 'Prawo karne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo administracyjne', 'Prawo administracyjne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Zarchiwizowana', 'Zarchiwizowana'), ('W toku', 'W toku'), ('Zadekretowana', 'Zadekretowana'), ('Czeka na dekretację', 'Czeka na dekretację'), ('Zakończona', 'Zakończona')]),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=25, upload_to=''),
        ),
    ]