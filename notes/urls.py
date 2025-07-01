from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from . import views_html

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path('notes-ui/', views_html.list_notes, name='list_notes'),
    path('notes-ui/create/', views_html.create_note, name='create_note'),
    path('notes-ui/edit/<int:note_id>/', views_html.edit_note, name='edit_note'),
    path('notes-ui/delete/<int:note_id>/', views_html.delete_note, name='delete_note'),
]


