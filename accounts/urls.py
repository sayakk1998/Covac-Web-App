from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('faq', views.faq, name='faq'),
    path('profile', views.profile, name='profile'),
    path('About', views.About, name='About'),
    path('feedback', views.feedback, name='feedback'),
    path('site', views.site, name='site')
]
