# Generated by Django 2.2.16 on 2022-02-27 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220227_1335'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='title',
            constraint=models.CheckConstraint(check=models.Q(year__lte=2022), name='year_lte_now'),
        ),
    ]
