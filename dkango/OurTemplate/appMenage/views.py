from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from statistics import mean
from .models import Personne,Prof

# Create your views here.

Menages = {
    "menage1": {"papa": 1800, "mama": 2500, "enfant11": 800, "enfant12": 1600},
    "menage2": {"papa": 0, "mama": 2800, "enfant21": 1100, "enfant22": 1500},
    "menage3": {"papa": 1800, "mama": 2500, "enfant31": 800, "enfant32" :1600,"enfant33" :1200},
    "menage4": {"papa": 1800, "mama": 2500},
    "menage5": {"mama": 2500,"enfant51": 1000, "enfant52": 1500},
    "menage6": {"papa": 1300, "mama": 2500, "enfant61": 800, "enfant62": 1600},
    "menage7": {"papa": 1800, "mama": 0, "enfant71": 800, "enfant72": 1600, "enfant73": 1200},
    "menage8": {"papa": 1800, "enfant81": 800, "enfant82": 1600, "enfant83": 1200},
}

def listeMenage(request):
    totMenage = {key:sum(value.values()) for key,value in Menages.items()}
    context={"revenu" : totMenage}

    template=loader.get_template("revenu.html")
    return HttpResponse(template.render(context,request))

def revenuMoyen(request):
    revMenage = {key:round(mean(value.values()),2) for key,value in Menages.items()}
    context={"revenuMoy" : revMenage}

    template=loader.get_template("revenuMoy.html")
    return HttpResponse(template.render(context,request))

def exoClassModel(request):
    personnes = Personne.objects.all().values()
    prof = Prof.objects.all().values()
    context={"personnes" : personnes,"prof" : prof}
    template=loader.get_template("classModel.html")
    return HttpResponse(template.render(context,request))
