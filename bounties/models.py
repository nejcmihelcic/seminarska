from django.db import models

# Create your models here.

class Subject(models.Model):
    """A subject the user is studying"""
    name=models.CharField(max_length=50)

    def __str__(self):
        """Returns string representation of name"""
        return self.name
    
class Topic(models.Model):
    """A topic the user is learning"""
    name=models.CharField(max_length=200)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Bounty(models.Model):
    """A topic a student needs help with"""
    name=models.CharField(max_length=200)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    text=models.TextField(default="Nedokoncana objava")

    class Meta:
        verbose_name_plural = 'bounties'

    def __str__(self):
        return self.name
