from django.db import models

# Create your models here.

class djangoClasses(models.Model):#defines a child of the Model parent class (the parent of all classes we make)
    #below we add class attributes that represent fields users can enter data into, which corrolate with our dB
    Title = models.CharField(max_length=100)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=255)
    Duration = models.FloatField()

    # this instantiates the Manager and stores it in objects to allow for dB queries and commands
    # to be issued by us against the dB, without using actual SQL language.
    objects = models.Manager()

