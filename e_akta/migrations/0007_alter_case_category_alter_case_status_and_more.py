# Generated by Django 4.2 on 2023-05-18 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0006_alter_case_category_alter_case_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo karne', 'Prawo karne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo cywilne', 'Prawo cywilne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Zakończona', 'Zakończona'), ('Zarchiwizowana', 'Zarchiwizowana'), ('W toku', 'W toku')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150),
        ),
    ]
