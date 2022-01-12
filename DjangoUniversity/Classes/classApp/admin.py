from django.contrib import admin

# Register your models here.

#you must import the model you created in models.py so that the admin.py can be aware of it when you refer to it here
from .models import djangoClasses

#this command is what allows you to see the class on the /admin website. You can also, from the site, do CRUD operations
#such as instantiating objects of the class, modifying those objects, or deleting them.
admin.site.register(djangoClasses)