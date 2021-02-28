from django.urls import path, include
from .views import index

app_name = 'socialnet'

urlpatterns = [
    path('', index, name='home'),
]