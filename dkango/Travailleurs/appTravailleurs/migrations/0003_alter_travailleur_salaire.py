# Generated by Django 5.0.3 on 2024-04-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTravailleurs', '0002_rename_travailleurs_travailleur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travailleur',
            name='salaire',
            field=models.IntegerField(),
        ),
    ]