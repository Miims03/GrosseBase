from django.urls import path
from . import views

urlpatterns = [
    path('affTrav', views.affTrav),
    path('saveTrav',views.saveTrav)

]