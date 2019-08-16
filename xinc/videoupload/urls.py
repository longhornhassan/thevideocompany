from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.uploadView, name='index'),
    path('upload/', views.upload_file, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)