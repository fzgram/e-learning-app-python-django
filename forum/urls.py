from django.urls import path
from . import views as forum_views

urlpatterns = [
    path('', forum_views.forum, name='forum'),
    path('<str:slug>/', forum_views.topic, name='topic'),
]
