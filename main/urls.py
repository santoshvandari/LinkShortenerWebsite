from django.urls import path
from main import views

urlpatterns = [
    path("", views.home,name="home"),
    path("home",views.home,name="home"),
    path('t/<slug>',views.shorturl,name="shorturl"),
]
