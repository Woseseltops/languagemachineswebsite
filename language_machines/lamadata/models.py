from django.db import models
from cms.models.fields import PlaceholderField
from publications.models import Publication
from django.conf import settings
import random

PERSON_FUNCTIONS = { 'head':'Department head','phd':'PhD Candidate','postdoc':'Postdoc','prof':'Professor','assistantprof':'Assistant Professor','programmer':'Scientific Programmer','intern':'Intern','master':'Master\'s Candidate', 'bachelor':'Bachelor\'s Candidate', 'guest':'Guest Researcher','sysadmin':'System Administrator' }
SOFTWARE_LICENSES = { 'gpl3': 'GNU Public License v3', 'gpl2': 'GNU Public License v2', 'agpl':'GPL Affero Public License v3','lgpl': 'Lesser GNU Public License v3', 'mit': 'MIT License', 'apache':'Apache License v2.0' }



class Person(models.Model):
    id = models.CharField("ID", help_text="ID, all lowercase and alphanumeric only, no spaces, will appear in URL like this", max_length=100, primary_key=True)
    firstname = models.CharField("First name", max_length=50)
    lastname = models.CharField("Last name", max_length=60)
    title = models.CharField("Title(s)", max_length=255, blank=True)
    nickname = models.CharField("Nickname", max_length=50, blank=True)
    affiliation = models.CharField("Affiliation", max_length=255,blank=True )
    function = models.CharField("Function", max_length=25,choices=sorted(PERSON_FUNCTIONS.items(), key= lambda x: x[1]))
    function2 = models.CharField("Secondary function", max_length=25,choices=sorted(PERSON_FUNCTIONS.items(), key=lambda x:x[1]), blank=True)
    interests = models.CharField("Interests", max_length=255,blank=True)
    email = models.CharField("E-mail", max_length=60)
    website = models.URLField("Website", max_length=60, blank=True)
    twitter = models.CharField("Twitter", max_length=60, blank=True)
    room = models.CharField("Room", max_length=60, blank=True)
    phone = models.CharField("Phone", max_length=60, blank=True)
    birth_date = models.DateField(blank=True,null=True)
    joined_date = models.DateField(blank=True,null=True)
    left_date = models.DateField(null=True,blank=True)
    description = models.TextField("Description",help_text="A short description about the person. For more text, use the content field.", blank=True)
    image = models.ImageField("Avatar",help_text="A 120x160 picture of the person, if not specified, you will be punished and a random llama will be shown.", upload_to='avatars/', blank=True, null=True)
    publications = models.ManyToManyField(Publication, blank=True)
    content = PlaceholderField('content')

    def __unicode__(self):
        return self.fullname()

    def getrandomlama(self):
        return settings.STATIC_URL +"/lama" + str(random.randint(1,6)) + ".jpg"

    def fullname(self):
        return self.firstname + " " + self.lastname

    def initialsname(self):
        return self.firstname[0] + ". " + self.lastname

    class Meta:
        ordering = ['firstname','lastname']

class Software(models.Model):
    id = models.CharField("ID", help_text="ID, all lowercase and alphanumeric only, no spaces, will appear in URL like this",max_length=100, primary_key=True)
    name = models.CharField("Name", max_length=100)
    website = models.URLField("Website", help_text="Link to the software's dedicated website", blank=True,null=True)
    source = models.URLField("Source code", help_text="Link to source code repository or download", blank=True,null=True)
    webservice = models.URLField("Webservice", help_text="Link to Webservice URL", blank=True, null=True)
    demo = models.URLField("Demo", help_text="Link to the demo URL", blank=True,null=True)
    documentation = models.URLField("Documentation", help_text="Link to where the documentation is hosted",blank=True,null=True)
    license = models.CharField("License",max_length=10, choices=sorted(SOFTWARE_LICENSES.items(), key=lambda x: x[1]) )
    description = models.TextField("Description",help_text="A short description about the software. For more text, use the content field.", blank=True)
    authors = models.ManyToManyField(Person)
    publications = models.ManyToManyField(Publication, blank=True)
    image = models.ImageField("Software Logo", upload_to='softwarelogos/', blank=True, null=True)
    content = PlaceholderField('content')


    class Meta:
        verbose_name_plural = "Software"
        ordering = ['name']

    def __unicode__(self):
        return self.name


class ProjectCategory(models.Model):
    id = models.CharField("ID", help_text="ID, all lowercase and alphanumeric only, no spaces, will appear in URL like this",max_length=100, primary_key=True)
    name = models.CharField("Category name", max_length=200)
    description = models.TextField("Description",help_text="A short description about the category.", blank=True)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
        ordering = ['name']


    def __unicode__(self):
        return self.name

class Project(models.Model):
    id = models.CharField("ID", help_text="ID, all lowercase and alphanumeric only, no spaces, will appear in URL like this",max_length=100, primary_key=True)
    name = models.CharField("Project name", max_length=100)
    category = models.ForeignKey(ProjectCategory, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(null=True,blank=True)
    sponsors = models.CharField("Sponsor(s)", max_length=255, blank=True)
    twitter = models.CharField("Twitter", max_length=60, blank=True)
    description = models.TextField("Description",help_text="A short description about the project. For more text, use the content field.", blank=True)
    members = models.ManyToManyField(Person, blank=True)
    software = models.ManyToManyField(Software, blank=True)
    publications = models.ManyToManyField(Publication, blank=True)
    image = models.ImageField("Project logo", upload_to='projectlogos/', blank=True, null=True)
    content = PlaceholderField('content')


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
