from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    """A subject the user is studying"""
    name=models.CharField(max_length=50)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns string representation of name"""
        return self.name
    
class Topic(models.Model):
    """A topic the user is learning"""
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Bounty(models.Model):
    """A topic a student needs help with"""
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    text=models.TextField(default="Nedokoncana objava")

    class Meta:
        verbose_name_plural = 'bounties'

    def __str__(self):
        return self.name

class Comment(models.Model):
    """The comment section on a bounty"""
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    bounty=models.ForeignKey(Bounty, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    text=models.TextField(default="Nedokoncana objava")

    def __str__(self):
        return self.text