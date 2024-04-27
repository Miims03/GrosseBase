from django.urls import path
from . import views

urlpatterns=[
    path('listeMenage',views.listeMenage),
    path('revenuMoyen',views.revenuMoyen),
    path('personnes',views.exoClassModel),
    ]