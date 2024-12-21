from django.urls import path 
from tutorials import views 

urlpatterns = [
    path('api/tutorials', views.tutorial_list),  # No need for regex
    path('api/tutorials/<int:pk>', views.tutorial_detail),  # Use <int:pk> for integer parameter
    path('api/tutorials/published', views.tutorial_list_published),
]