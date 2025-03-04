from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from myapp.serializers import UserCreationSerializer,MealSerializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
from myapp.models import Meal
from rest_framework import serializers
from rest_framework.views import APIView
from django.db.models import Sum
# Create your views here.

class UserCreationView(CreateAPIView):

    serializer_class=UserCreationSerializer

class MealListCreateView(ListCreateAPIView):
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[authentication.BasicAuthentication]

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MealDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.BasicAuthentication]

    def get(self, request, *args, **kwargs):
        meals = Meal.objects.filter(user=request.user)

        # Apply filters if query parameters are provided
        date = request.query_params.get("date")
        meal_type = request.query_params.get("meal_type")

        if date:
            meals = meals.filter(date=date)
        if meal_type:
            meals = meals.filter(meal_type=meal_type)

        meal_data = meals.values("name", "meal_type", "calories", "date")

        return Response(data=meal_data)
    
class TotalCalorieView(APIView):

    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.BasicAuthentication]

    def get(self,request,*args,**kwargs):

        total_calories=Meal.objects.filter(user=request.user).aggregate(total=Sum("calories"))


        return Response({
            "total_calories": total_calories,
        })