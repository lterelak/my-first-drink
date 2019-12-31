# Generated by Django 2.1.5 on 2019-12-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=250)),
                ('preparation', models.CharField(max_length=1000)),
                ('recipe_image', models.ImageField(default='', upload_to='images/')),
                ('ingredients', models.ManyToManyField(to='drinks.Ingredient')),
            ],
        ),
    ]
