from django.urls import path

from .views import ish_olish, main, worker

urlpatterns = [
    path('', main, name='user'),
    path('worker/', worker, name='worker'),
    path('ish/', ish_olish, name='ish'),
    
]