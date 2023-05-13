# Generated by Django 4.2 on 2023-05-12 13:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0021_alter_case_category_alter_case_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo karne', 'Prawo karne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo cywilne', 'Prawo cywilne'), ('Prawo rodzinne', 'Prawo rodzinne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Zakończona', 'Zakończona'), ('Zarchiwizowana', 'Zarchiwizowana'), ('W toku', 'W toku')]),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(max_length=25, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
