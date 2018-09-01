from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='%(class)s_req_3', on_delete=models.CASCADE,)
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    age = models.PositiveSmallIntegerField()
    image = models.URLField(max_length=500,blank=True, null=True)

    def __str__(self):
        return self.user.first_name

class Form(models.Model):
    name = models.CharField( max_length=50)
    shape = models.CharField( max_length=50)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    SYMBOL_CHOICES = (
        (None, 'Choose symbol'),
        ('1', 'Default'),
        ('3', 'Symbol_1'),
        ('2', 'Symbol_2'),
    )
    project_name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    form_submitted = models.PositiveSmallIntegerField(blank=True, null=True)
    total = models.PositiveSmallIntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    last_updated_on = models.DateTimeField(auto_now=True, blank=True)
    count = models.PositiveSmallIntegerField(blank=True, null=True)
    profile = models.ManyToManyField(Profile,related_name='%(class)s_req_1',blank=True)
    forms = models.ManyToManyField(Form, related_name='%(class)s_req_2',blank=True)
    symbol = models.CharField(max_length=10, choices=SYMBOL_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.project_name


