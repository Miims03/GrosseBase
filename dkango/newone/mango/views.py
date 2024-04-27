from django.shortcuts import render
from .models import Fruit
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .formFruit import formFruit


# Create your views here.

def showFruit(request):
    if request.method == 'POST':
        form = formFruit(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:    
        form = formFruit
    fruit = Fruit.objects.all().values()
    template = loader.get_template('fruit.html.twig')
    context = {
        'fruit' : fruit,
        'form' : form
    }
    return HttpResponse(template.render(context, request))