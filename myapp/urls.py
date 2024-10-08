from django.urls import path
from myapp import views
urlpatterns = [
    path('user/',views.user,name="user"),
    path('genre/',views.genre,name="genra")
]