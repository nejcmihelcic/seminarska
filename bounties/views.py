from django.shortcuts import render, redirect
from .models import Subject, Topic, Bounty, Comment
from. forms import BountyForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
    comments=bounty.comment_set.all()
    context={'bounty': bounty, 'comments': comments, 'topic_id': topic_id}
    return render(request, 'bounties/bounty.html', context)

@login_required
def new_bounty(request, topic_id):
    """Returns page for creating a new bounty"""
    topic=Topic.objects.get(id=topic_id)
    subject=topic.subject

    if request.method != 'POST':
        #No data submitted; create blank form.
        form=BountyForm()
    else:
        #Post data submitted; process data.
        form=BountyForm(data=request.POST)
        if form.is_valid():
            new_bounty=form.save(commit=False)
            new_bounty.topic = topic
            new_bounty.subject = subject
            new_bounty.owner = request.user
            new_bounty.save()
            return redirect('bounties:topic', topic_id=topic_id)
        
    #Display blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'bounties/new_bounty.html', context)

@login_required
def edit_bounty(request, bounty_id):
    """Edit an existing bounty"""
    bounty=Bounty.objects.get(id=bounty_id)
    if bounty.owner != request.user:
        raise Http404
    topic=bounty.topic

    if request.method != 'POST':
        # initial reqest
        form = BountyForm(instance=bounty)
    else:
        # post data submitted
        form=BountyForm(instance=bounty, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bounties:topic', topic_id=topic.id)
        
    context = {'bounty': bounty, 'topic': topic, 'form': form}
    return render(request, 'bounties/edit_bounty.html', context)

@login_required
def new_comment(request, topic_id, bounty_id):
    """Returns comment creation page"""
    bounty=Bounty.objects.get(id=bounty_id)

    if request.method != 'POST':
        #no post data, make empty form
        form=CommentForm()
    else:
        form=CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.owner = request.user
            new_comment.bounty=bounty
            new_comment.save()
            return redirect('bounties:bounty', topic_id=topic_id, bounty_id=bounty_id)
    
    context={'form': form, 'bounty': bounty, 'topic_id': topic_id}
    
    #Display blank / invalid form
    return render(request, 'bounties/new_comment.html', context)

@login_required
def edit_comment(request, bounty_id, comment_id):
    """edit an existing comment"""
    comment=Comment.objects.get(id=comment_id)
    bounty=Bounty.objects.get(id=bounty_id)
    if comment.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = CommentForm(instance=comment)
    else:
        form=CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bounties:bounty', topic_id=bounty.topic.id, bounty_id=bounty.id)
        
    context = {'comment': comment, 'bounty': bounty, 'form': form}
    return render(request, 'bounties/edit_comment.html', context)
    
