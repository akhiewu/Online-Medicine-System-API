# Generated by Django 4.0.2 on 2022-02-08 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_medicinecategory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicine',
        ),
    ]