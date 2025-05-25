from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, index, add_note, signup, user_login,delete_note

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('add/', add_note, name='add_note'),
    path('api/', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('delete/<int:note_id>/', delete_note, name='delete_note'),  # assumes you renamed your view to user_login
]
