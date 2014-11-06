# Create your views here.
from django.http import Http404
from django.shortcuts import render_to_response

from language_machines.lamadata.models import Person, Software, Project

def personindex(request):
    return render_to_response('personindex.html', {'persons': Person.objects.all()})

def projectindex(request):
    return render_to_response('projectindex.html', {'projects': Project.objects.all()})

def softwareindex(request):
    return render_to_response('softwareindex.html', {'softwares': Software.objects.all()})

def personview(request, person_id):
    return render_to_response('personview.html', {'person': Person.objects.get(pk=person_id)})

def projectview(request, project_id):
    return render_to_response('projectview.html', {'project': Project.objects.get(pk=project_id)})

def softwareview(request, software_id):
    return render_to_response('softwareview.html', {'software': Software.objects.get(pk=software_id)})
