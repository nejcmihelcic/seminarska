from django.contrib import admin

# Register your models here.
from .models import Subject, Topic, Bounty, Comment

admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Bounty)
admin.site.register(Comment)