from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('gallery/', views.GalleryPageView.as_view(), name='gallery'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts'),
]