# Generated by Django 2.1.5 on 2020-01-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='drinks.Ingredient'),
        ),
    ]
