from django.shortcuts import render
from .models import Folder


def folder_view(request):
    folders = Folder.objects.all()
    return render(request, 'folders/folder_view.html', {'folders': folders})
