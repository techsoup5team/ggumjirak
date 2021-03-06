from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home),
    path('schedule/', views.schedule),
    path('donation/', views.donation),
    path('blog/', views.blog),
    path('blog/<int:pk>/',views.posting, name='posting'),
    path('contact/', views.contact),
    path('board/', views.board),
    path('ci/', views.ci),
    path('greeting/', views.greeting),
    path('rounding/', views.rounding),

    path('notice/', views.notice),
    path('notice/<int:pk>/',views.notice_posting, name='notice_posting'),

    path('donat_report/', views.donat_report),
    path('donat_report/<int:pk>/',views.donat_posting, name='donat_report_posting'),

    path('history/', views.history),
    path('history/<int:pk>/',views.history_posting, name='history_posting'),

    path('project/', views.project),
    path('project/<int:pk>/',views.project_posting, name='project_posting'),

    path('news/', views.news),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

