from django.urls import path
from . import views
urlpatterns = [
    path('slotbook', views.slotbook, name='slotbook'),
    path('confirm', views.confirm, name='confirm')


]