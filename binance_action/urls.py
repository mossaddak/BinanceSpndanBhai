from binance_action import views
from django.urls import path

urlpatterns = [
    path('connection/', views.binance_connection, name="binance_connection"),
]