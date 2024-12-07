# Generated by Django 5.1.3 on 2024-12-05 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0004_alter_drivers_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='rating',
            field=models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE'), ('4', 'FOUR'), ('5', 'FIVE')], default='5', max_length=20),
        ),
    ]
