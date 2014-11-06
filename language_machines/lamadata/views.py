# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from language_machines.lamadata.models import Person, Software, Project

def personindex(request):
    return render_to_response('personindex.html', {'persons': Person.objects.all()}, context_instance=RequestContext(request) )

def projectindex(request):
    return render_to_response('projectindex.html', {'projects': Project.objects.all()}, context_instance=RequestContext(request) )

def softwareindex(request):
    return render_to_response('softwareindex.html', {'softwares': Software.objects.all()}, context_instance=RequestContext(request) )

def personview(request, person_id):
    return render_to_response('personview.html', {'person': Person.objects.get(pk=person_id)}, context_instance=RequestContext(request) )

def projectview(request, project_id):
    return render_to_response('projectview.html', {'project': Project.objects.get(pk=project_id)}, context_instance=RequestContext(request) )

def softwareview(request, software_id):
    return render_to_response('softwareview.html', {'software': Software.objects.get(pk=software_id)}, context_instance=RequestContext(request) )

def publicationindex(request, publication_id):
    pass

def publicationview(request, publication_id):
    pass
