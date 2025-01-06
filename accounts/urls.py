from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.registration.as_view(), name='registration'), 
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]