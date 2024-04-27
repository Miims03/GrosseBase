from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

D = {
    "Anne":30,
    "Jean":45,
    "Pierre":65,
    "Bosco":65
    }

def LsterPersonne(request):
    template=loader.get_template("personne.html")
    context={"myDict":D}
    return HttpResponse(template.render(context,request))
