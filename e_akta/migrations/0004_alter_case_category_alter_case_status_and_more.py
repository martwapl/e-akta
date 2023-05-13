# Generated by Django 4.2 on 2023-05-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0003_alter_case_category_alter_case_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo karne', 'Prawo karne'), ('Prawo cywilne', 'Prawo cywilne'), ('Prawo pracy', 'Prawo pracy')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Czeka na dekretację', 'Czeka na dekretację'), ('Zarchiwizowana', 'Zarchiwizowana'), ('Zakończona', 'Zakończona'), ('Zadekretowana', 'Zadekretowana'), ('W toku', 'W toku')]),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=25, upload_to=''),
        ),
    ]
