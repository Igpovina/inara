# Generated by Django 4.1.2 on 2022-10-27 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InaraApp', '0002_rename_member_since_commander_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='type',
            field=models.CharField(choices=[('CORIOLIS', 'Coriolis'), ('ORBITAL', 'Orbital'), ('REFINERY', 'Refinery'), ('PLANETARY', 'Planetary')], max_length=30),
        ),
    ]
