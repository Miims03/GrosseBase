from django.shortcuts import render
from .models import myStudents
from django.template import loader
from django.http import HttpResponse
from .formStudents import formulaireStudents


# Create your views here.

def afficherStudents(request):
    students=myStudents.objects.all().values()
    template=loader.get_template("students.html")
    context={"students":students}
    return HttpResponse(template.render(context,request))

def saveStudents(request):
    if request.method=='POST':
        form=formulaireStudents(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('save successfully')
    else:
        form=formulaireStudents()
    template=loader.get_template('formulaireEtudiant.html') 
    context={'form':form}  
    return HttpResponse(template.render(context,request))    


