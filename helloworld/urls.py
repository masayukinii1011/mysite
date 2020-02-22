from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloworldfunction),  # views.pyのhelloworldfunctionへ
]
