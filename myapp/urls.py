from django.urls import path
from myapp import views

urlpatterns=[
    path('register/',views.UserCreationView.as_view()),
    path("meals/",views.MealListCreateView.as_view()),
    path('details/',views.MealDetailView.as_view()),
    path('calories/',views.TotalCalorieView.as_view())
]