from django.shortcuts import render
from .models import Subject, Topic

# Create your views here.
def index(request):
    """Home page for encoded"""
    return render(request, 'bounties/index.html')

def subjects(request):
    """Returns list of all subjects"""
    subjects=Subject.objects.order_by('name')
    context={'subjects': subjects}
    return render(request, 'bounties/subjects.html', context)

def subject(request, subject_id):
    """return page for a specific subject"""
    subject=Subject.objects.get(id=subject_id)
    topics=subject.topic_set.all()
    context = {'subject': subject, 'topics': topics}
    return render(request, 'bounties/subject.html', context)

def topic(request, topic_id):
    """Return page containing bounties for current topic"""
    topic=Topic.objects.get(id=topic_id)
    bounties=topic.bounty_set.order_by('-date_added')
    context={'topic': topic, 'bounties': bounties}
    return render(request, 'bounties/topic.html', context)

def bounty(request, topic_id, bounty_id):
    """Return page for specific bounty"""
    topic=Topic.objects.get(id=topic_id)
    bounty=topic.bounty_set.get(id=bounty_id)
    context={'bounty': bounty}
    return render(request, 'bounties/bounty.html', context)