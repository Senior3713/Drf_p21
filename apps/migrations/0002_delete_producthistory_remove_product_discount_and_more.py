# Generated by Django 5.0.7 on 2024-09-12 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductHistory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
    ]
