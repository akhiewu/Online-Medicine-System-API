# Generated by Django 4.0.2 on 2022-02-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0004_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicinecategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
