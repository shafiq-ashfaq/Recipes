# Generated by Django 4.2.3 on 2023-09-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0002_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_decription', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='Recipe')),
            ],
        ),
    ]