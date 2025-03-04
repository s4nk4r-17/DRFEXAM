from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meal(models.Model):

    MEAL_TYPES=[
        ('Breakfast','Breakfast'),
        ('Dinner','Dinner'),
        ('Lunch','Lunch'),
        ('Snack','Snack'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    calories=models.IntegerField()
    meal_type=models.CharField(choices=MEAL_TYPES,max_length=10)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -{self.meal_type} {self.date}"