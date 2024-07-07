from django.urls import path
from .views import folder_view

urlpatterns = [
    path('folders/', folder_view, name='folder_view'),
]
