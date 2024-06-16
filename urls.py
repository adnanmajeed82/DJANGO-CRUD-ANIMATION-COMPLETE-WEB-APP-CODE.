from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.animation_list, name='animation_list'),
    path('animation/<int:pk>/', views.animation_detail, name='animation_detail'),
    path('animation/new/', views.animation_create, name='animation_create'),
    path('animation/<int:pk>/edit/', views.animation_update, name='animation_update'),
    path('animation/<int:pk>/delete/', views.animation_delete, name='animation_delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)