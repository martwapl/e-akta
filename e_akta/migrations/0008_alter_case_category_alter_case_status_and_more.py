# Generated by Django 4.2 on 2023-05-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0007_alter_case_category_alter_case_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='category',
            field=models.CharField(choices=[('Prawo karne', 'Prawo karne'), ('Prawo rodzinne', 'Prawo rodzinne'), ('Prawo pracy', 'Prawo pracy'), ('Prawo administracyjne', 'Prawo administracyjne'), ('Prawo cywilne', 'Prawo cywilne')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('Zarchiwizowana', 'Zarchiwizowana'), ('W toku', 'W toku'), ('Zakończona', 'Zakończona')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]