"""Defines urls for encoded"""

from django.urls import path

from . import views

app_name='bounties'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    
    #page that shows all subjects
    path('subjects/', views.subjects, name='subjects'),

    #page that shows a specific subject and its corresponding topics
    path('subjects/<int:subject_id>/', views.subject, name='subject'),

    #lists specific topic and its bounties
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #lists bounty
    path('topic/<int:topic_id>/<int:bounty_id>', views.bounty, name='bounty'),
    
    #adds a new bounty
    path('new_bounty/<int:topic_id>/', views.new_bounty, name='new_bounty'),

    #edits an existing bounty
    path('edit_bounty/<int:bounty_id>/', views.edit_bounty, name='edit_bounty'),
]