from django.urls import path
from . import views

urlpatterns = [
 path('iteams/', views.show_item, name = 'iteam'),
]
