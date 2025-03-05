# Generated by Django 5.1.6 on 2025-03-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), ('Snack', 'Snack'), ('Dinner', 'Dinner')], default='Breakfast', max_length=100),
        ),
    ]
