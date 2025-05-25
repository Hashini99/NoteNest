# from rest_framework.routers import DefaultRouter
# from .views import NoteViewSet
# from django.urls import path, include  # ✅ include is important

# router = DefaultRouter()
# router.register(r'notes', NoteViewSet)

# urlpatterns = [
#     path('', include(router.urls)),  # ✅ include the router.urls, not the router itself
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
