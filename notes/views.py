
# # notes/views.py
# from django.shortcuts import render, redirect

# from notes.serializers import NoteSerializer
# from .models import Note
# from .forms import NoteForm
# from rest_framework import viewsets
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate

# def index(request):
#     notes = Note.objects.order_by('-created_at')
#     return render(request, 'notes/index.html', {'notes': notes})

# def add_note(request):
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = NoteForm()
#     return render(request, 'notes/note_form.html', {'form': form})

# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

#     # Signup View
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to a home page or wherever you want after signup
#     else:
#         form = UserCreationForm()
#     return render(request, 'your_app/signup.html', {'form': form})

# # Login View
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')  # Redirect to the home page or a dashboard after login
#     else:
#         form = AuthenticationForm()
#     return render(request, 'your_app/login.html', {'form': form})



# notes/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .models import Note
from .forms import NoteForm
from .serializers import NoteSerializer
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
# Home Page (list of notes)
@login_required
def index(request):
    notes = Note.objects.order_by('-created_at')
    return render(request, 'notes/index.html', {'notes': notes})

# Add Note View
@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # You should define a URL name 'home' pointing to index()
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

# DRF API View
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'notes/signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'notes/login.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        note.delete()  # Delete the note
        return redirect('home') 