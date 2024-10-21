from django.urls import path, re_path
from notes_app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('user/', views.userApi),
    path('user/<int:id>', views.userApi),

    path('profile/', views.profileApi),
    path('profile/<int:id>', views.profileApi),

    path('subject/', views.subjectApi),
    path('subject/<int:id>', views.subjectApi),

    path('tag/', views.tagApi),
    path('tag/<int:id>', views.tagApi),

    path('note/', views.noteApi),
    path('note/<int:id>', views.noteApi),

    path('note_tag/', views.noteTagApi),
    path('note_tag/<int:id>', views.noteTagApi),

    path('note_subject/', views.noteSubjectApi),
    path('note_subject/<int:id>', views.noteSubjectApi),

    path('save_file', views.saveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
