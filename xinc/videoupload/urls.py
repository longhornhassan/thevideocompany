from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.uploadView, name='index'),
    path('upload/', views.upload_file, name='index'),
    path('name/', views.get_name, name='index'),
    path('uploadFile/', views.write_file, name='index'),
    path('filelist/', views.file_list, name='index'),
    path('watch/<name>/', views.watch_video),

    #DEBUGGING
    path('clear/', views.clear_database),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)