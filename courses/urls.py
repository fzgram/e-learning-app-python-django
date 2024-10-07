from django.urls import path
from . import views as course_views
from users import views as user_views

urlpatterns = [
    path('', course_views.courses, name='courses'),

    path('student/<str:course_name>/', user_views.course_homepage, name='course_homepage'),
    path('student/(<str:course_name>/<str:slug>/', user_views.student_course,
        name='student_course'),

    path('professor/<str:course_name>/', course_views.course, name='professor_course'),
    path('professor/<str:course_name>/delete/', course_views.delete_course, name='delete'),
    path('professor/<str:course_name>/edit/', course_views.update_course, name='edit'),

    path('professor/<str:course_name>/students/', course_views.list_students, name='list_students'),
    path('professor/<str:course_name>/students/<str:student_id>[\d ]+)/remove/',
        course_views.remove_students, name='remove_students'),
    path('professor/<str:course_name>/students/<str:student_id>[\d ]+)/add/',
        course_views.add_students, name='add_students'),

    path('professor/<str:course_name>/<str:slug>/', course_views.chapter, name='chapter'),
    path('professor/edit/<str:course_name>/<str:slug>/',
        course_views.update_chapter, name='edit_chapter'),
    path('professor/delete/<str:course_name>/<str:slug>/',
        course_views.delete_chapter, name='delete_chapter'),

    path('professor/<str:course_name>/<str:slug>[\w-]+)/<str:txt_id>[\d ]+)/txt/edit/',
        course_views.update_text_block, name='edit_txt'),
    path('professor/txt/delete/<str:txt_id>[\d ]+)/', course_views.delete_text_block, name='delete_txt'),

    path('professor/<str:course_name>/<str:slug>[\w-]+)/<str:yt_id>[\d ]+)/link/edit/',
        course_views.update_yt_link, name='edit_link'),
    path('professor/link/delete/<str:yt_id>[\d ]+)/', course_views.delete_yt_link, name='delete_link'),

    path('professor/file/delete/<str:file_id>[\d ]+)/', course_views.delete_file, name='delete_file'),
]
