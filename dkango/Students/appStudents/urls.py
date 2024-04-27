from django.urls import path
from . import views




urlpatterns=[path('afficherStudents', views.afficherStudents),
             path('saveStudents',views.saveStudents)
             ]