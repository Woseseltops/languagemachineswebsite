# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from language_machines.lamadata.models import Person, Software, Project
from publications.models import Publication
from django.db.models import Q


def personindex(request):
    return render_to_response('personindex.html', {'persons': Person.objects.order_by('joined_date','firstname')}, context_instance=RequestContext(request) )

def projectindex(request):
    return render_to_response('projectindex.html', {'projects': Project.objects.order_by('name')}, context_instance=RequestContext(request) )

def softwareindex(request):
    return render_to_response('softwareindex.html', {'softwares': Software.objects.order_by('name')}, context_instance=RequestContext(request) )

def personview(request, person_id):
    person = Person.objects.get(pk=person_id)
    softwares = Software.objects.filter(authors__id=person_id)
    projects = Project.objects.filter(members__id=person_id)
    publications = Publication.objects.filter(Q(authors__contains=person.initialsname()) | Q(authors__contains=person.fullname()) )
    return render_to_response('personview.html', {'person': person, 'softwares': softwares, 'projects': projects, 'publications': publications }, context_instance=RequestContext(request) )

def projectview(request, project_id):
    return render_to_response('projectview.html', {'project': Project.objects.get(pk=project_id)}, context_instance=RequestContext(request) )

def softwareview(request, software_id):
    projects = Project.objects.filter(software__id=software_id)
    return render_to_response('softwareview.html', {'software': Software.objects.get(pk=software_id), 'projects': projects}, context_instance=RequestContext(request) )

def publicationindex(request, publication_id):
    pass

def publicationview(request, publication_id):
    pass
