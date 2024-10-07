from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.profile, name='profile'),
    path('student/$', user_views.student, name='student'),
    path('professor/$', user_views.professor, name='professor'),

    path('admin/$', user_views.admin, name='admin'),
    path('edit/(?P<username>[\w ]+)/$', user_views.update_user, name='update_user'),
    path('delete/(?P<username>[\w ]+)/$', user_views.delete_user, name='delete_user'),
]
