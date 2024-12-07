# Generated by Django 5.1.3 on 2024-12-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0003_alter_drivers_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='rating',
            field=models.CharField(choices=[('ONE', '1'), ('TWO', '2'), ('THREE', '3'), ('FOUR', '4'), ('FIVE', '5')], default='5', max_length=20),
        ),
    ]
