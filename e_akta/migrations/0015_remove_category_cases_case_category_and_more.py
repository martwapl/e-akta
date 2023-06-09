# Generated by Django 4.2 on 2023-05-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_akta', '0014_alter_case_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cases',
        ),
        migrations.AddField(
            model_name='case',
            name='category',
            field=models.ManyToManyField(to='e_akta.category'),
        ),
        migrations.AlterField(
            model_name='case',
            name='status',
            field=models.CharField(choices=[('W toku', 'W toku'), ('Zakończona', 'Zakończona'), ('Zarchiwizowana', 'Zarchiwizowana')]),
        ),
    ]
