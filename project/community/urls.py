from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('schedule/', views.schedule),
    path('donation/', views.donation),
    path('beta/', views.beta),
    path('gamma/', views.gamma),
    path('blog/', views.blog),
    path('blog/<int:pk>/',views.posting, name='posting'),
]