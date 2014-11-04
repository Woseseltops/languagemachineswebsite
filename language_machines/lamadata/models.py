from django.db import models
from cms.models.pluginmodel import CMSPlugin
from publications.models import Publication

PERSON_FUNCTIONS = { 'phd':'PhD Candidate','postdoc':'Postdoc','prof':'Professor','assistantprof':'Assistant Professor','programmer':'Scientific Programmer','intern':'Intern','master':'Master\'s Candidate', 'bachelor':'Bachelor\'s Candidate', 'guest':'Guest Researcher' }
SOFTWARE_LICENSES = { 'gpl3': 'GNU Public License v3', 'gpl2': 'GNU Public License v2', 'agpl':'GPL Affero Public License v3','lgpl': 'Lesser GNU Public License v3', 'mit': 'MIT License', 'apache':'Apache License v2.0' }



class Person(models.Model):
    firstname = models.CharField("First name", max_length=50)
    lastname = models.CharField("Last name", max_length=60)
    title = models.CharField("Title(s)", max_length=255)
    nickname = models.CharField("Nickname", max_length=50, blank=True)
    affiliation = models.CharField("Affiliation", max_length=255)
    function = models.CharField("Function", max_length=25,choices=PERSON_FUNCTIONS.items())
    function2 = models.CharField("Secondary function", max_length=25,choices=PERSON_FUNCTIONS.items())
    interests = models.CharField("Interests", max_length=255)
    email = models.CharField("E-mail", max_length=60)
    website = models.URLField("Website", max_length=60)
    twitter = models.CharField("Twitter", max_length=60)
    room = models.CharField("Room", max_length=60)
    phone = models.CharField("Phone", max_length=60)
    birth_date = models.DateField()
    joined_date = models.DateField()
    left_date = models.DateField(null=True,blank=True)
    description = models.TextField("Description",help_text="A short description about the person. For more text, use the dedicated page.")
    image = models.ImageField("Avatar",upload_to='avatars/', blank=True, null=True)
    publications = models.ManyToManyField(Publication)

    def getslug(self):
        fullname = self.firstname + " " + self.lastname
        return fullname.replace(" ", "-")


class Software(models.Model):
    name = models.CharField("Name", max_length=100)
    Website = models.URLField("Website", help_text="Link to the software's dedicated website", blank=True,null=True)
    source = models.URLField("Source code", help_text="Link to source code repository or download", blank=True,null=True)
    webservice = models.URLField("Webservice", help_text="Link to Webservice URL", blank=True, null=True)
    demo = models.URLField("Demo", help_text="Link to the demo URL", blank=True,null=True)
    documentation = models.URLField("Documentation", help_text="Link to where the documentation is hosted",blank=True,null=True)
    license = models.CharField("License",max_length=10, choices=SOFTWARE_LICENSES.items())
    description = models.TextField("Description",help_text="A short description about the software. For more text, use the dedicated page.")
    authors = models.ManyToManyField(Person)
    publications = models.ManyToManyField(Publication)
    image = models.ImageField("Software Logo", upload_to='softwarelogos/', blank=True, null=True)

    def getslug(self):
        return self.name.replace(" ", "-")

    class Meta:
        verbose_name_plural = "Software"

class Project(models.Model):
    name = models.CharField("Project name", max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True,blank=True)
    sponsors = models.CharField("Sponsor(s)", max_length=255)
    twitter = models.CharField("Twitter", max_length=60)
    description = models.TextField("Description",help_text="A short description about the project. For more text, use the dedicated page.")
    members = models.ManyToManyField(Person)
    software = models.ManyToManyField(Software)
    publications = models.ManyToManyField(Publication)
    image = models.ImageField("Project logo", upload_to='projectlogos/', blank=True, null=True)

    def getslug(self):
        return self.name.replace(" ", "-")

class PersonView(CMSPlugin):
    person = models.ForeignKey(Person)

class SoftwareView(CMSPlugin):
    software = models.ForeignKey(Software)

class ProjectView(CMSPlugin):
    project = models.ForeignKey(Project)

class SoftwareIndex(CMSPlugin):
    viewtype = models.CharField(max_length=1, choices=( ('all',"All"), ("webservices",'Webservices'), ('demos','Demos') ) )


