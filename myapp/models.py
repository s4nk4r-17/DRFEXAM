from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Meal(models.Model):

    name=models.CharField(max_length=200)

    MEAL_TYPES=[
        ('Breakfast','Breakfast'),
        ('Brunch','Brunch'),
        ('Lunch','Lunch'),
        ('Snack','Snack'),
        ('Dinner','Dinner')
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    calories=models.IntegerField()
    meal_type=models.CharField(choices=MEAL_TYPES,max_length=100,default='Breakfast')
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return self.name