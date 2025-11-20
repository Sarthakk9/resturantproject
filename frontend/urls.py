from django.urls import path
from . import views
app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('chef/', views.chef, name='chef'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
]
