"""Defines urls for encoded"""

from django.urls import path

from . import views

app_name='bounties'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    
    #Subjects
    path('subjects/', views.subjects, name='subjects'),
    #Topics
    path('subjects/<int:subject_id>/', views.subject, name='subject'),
   
    #Bounties
    path('topics/<int:topic_id>/', views.topic, name='topic'),    
    path('topic/<int:topic_id>/<int:bounty_id>', views.bounty, name='bounty'),
    path('new_bounty/<int:topic_id>/', views.new_bounty, name='new_bounty'),
    path('edit_bounty/<int:bounty_id>/', views.edit_bounty, name='edit_bounty'),

    #comments
    path('add_comment/<int:topic_id>/<int:bounty_id>/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:bounty_id>/<int:comment_id>/', views.edit_comment, name='edit_comment'),

]