from django.shortcuts import render
from .models import Travailleur
from django.template import loader
from django.http import HttpResponse
from .formTravailleur import formTravailleur
 
# Create your views here.

def affTrav(request):
    travailleur = Travailleur.objects.all().values()
    template = loader.get_template('travailleur.html')
    context = {'travailleur' : travailleur}
    return HttpResponse(template.render(context,request))

def saveTrav(request):
    if request.method == 'POST':
        form = formTravailleur(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('save success')
    else:
        form = formTravailleur()
    template = loader.get_template('travailleur.html')
    context = {'form' : form}
    return HttpResponse(template.render(context,request))
