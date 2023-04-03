from django.contrib import admin

# Register your models here.
from .models import Subject, Topic, Bounty

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Bounty)