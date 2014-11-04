from django.db import models


PERSON_FUNCTIONS = { 'phd':'PhD Candidate','postdoc':'Postdoc','prof':'Professor','assistantprof':'Assistant Professor','programmer':'Scientific Programmer','intern':'Intern','master':'Master\'s Candidate', 'bachelor':'Bachelor\'s Candidate' }
SOFTWARE_LICENSES = { 'gpl3': 'GNU Public License v3', 'gpl2': 'GNU Public License v2', 'agpl':'GPL Affero Public License v3','lgpl': 'Lesser GNU Public License v3', 'mit': 'MIT License', 'apache':'Apache License v2.0' }


# Create your models here.
class Person(models.Model):
    firstname = models.CharField("First name", max_length=50)
    lastname = models.CharField("Last name", max_length=60)
    title = models.CharField("Title(s)", max_length=255)
    nickname = models.CharField("Nickname", max_length=50, blank=True)
    affiliation = models.CharField("Affiliation", max_length=255)
    function = models.CharField("Function", max_length=25,choices=PERSON_FUNCTIONS.items())
    function2 = models.CharField("Secondary function", max_length=25,choices=PERSON_FUNCTIONS.items())
    email = models.CharField("E-mail", max_length=60)
    website = models.CharField("Website", max_length=60)
    twitter = models.CharField("Twitter", max_length=60)
    room = models.CharField("Room", max_length=60)
    phone = models.CharField("Phone", max_length=60)
    birth_date = models.DateField()
    joined_date = models.DateField()
    left_date = models.DateField(null=True,blank=True)
    description = models.TextField("Description",help="A short description about the person. For more text, use the dedicated page.")


class Project(models.Model):
    name = models.CharField("Project name", max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    sponsors = models.CharField("Sponsor(s)", max_length=255)
    twitter = models.CharField("Twitter", max_length=60)
    description = models.TextField("Description",help="A short description about the project. For more text, use the dedicated page.")
    members = models.ManyToManyField(Person)
    software = models.ManyToManyField(Person)

class Sofware(models.Model):
    name = models.CharField("Project name", max_length=100)
    Website = models.CharField("Website", max_length=250)
    source = models.CharField("Source code", max_length=250)
    documentation = models.CharField("Documentation", max_length=250)
    license = models.charfield("License",max_length=10, choices=SOFTWARE_LICENSES.items())
    description = models.TextField("Description",help="A short description about the software. For more text, use the dedicated page.")
    authors = models.ManyToManyField(Person)


