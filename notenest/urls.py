

# notenest/urls.py

# from django.contrib import admin
# from django.urls import path, include
# from notes import views  
# from django.shortcuts import redirect
# from django.contrib.auth.decorators import login_required
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', lambda request: redirect('login')),
#     path('', views.index, name='home'),           # ROOT path → index view
#     path('add/', views.add_note, name='add_note'), # add note form
#     path('api/', include('notes.api_urls')),       # API routes (if any)
# ]
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # root path redirects to login
    path('notes/', include('notes.urls')),        # all app URLs come from notes.urls
]
