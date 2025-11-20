from django.urls import path
from . import views

app_name = 'backend'  

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # MENU
    path('dashboard/menu/', views.menu_list, name='menu_list'),
    path('dashboard/menu/add/', views.add_menu_item, name='add_menu_item'),
    path('dashboard/menu/edit/<int:id>/', views.edit_menu_item, name='edit_menu_item'),
    path('dashboard/menu/delete/<int:id>/', views.delete_menu_item, name='delete_menu_item'),

    # ABOUT 
    path('dashboard/about/', views.about_list, name='about_list'),
    path('dashboard/about/edit/<int:pk>/', views.about_edit, name='about_edit'),
    path('dashboard/about/delete/<int:pk>/', views.about_delete, name='about_delete'),
    path('dashboard/about/add/', views.about_add, name='about_add'),

    # BLOG
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/add/', views.blog_add, name='blog_add'),
    path('blogs/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),

    # CHEF
  
    path('dashboard/chef/', views.chef_list, name='chef_list'),
    path('dashboard/chef/add/', views.add_chef, name='add_chef'),
    path('dashboard/chef/edit/<int:pk>/', views.edit_chef, name='edit_chef'),
    path('dashboard/chef/delete/<int:pk>/', views.delete_chef, name='delete_chef'),
    # UI PAGES
    path('buttons/', views.buttons, name='buttons'),
    path('typography/', views.typography, name='typography'),
    path('elements/', views.elements, name='elements'),
    path('charts/', views.charts, name='charts'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('404/', views.error_404, name='error_404'),
    path('blank/', views.blank, name='blank'),
    # AUTHENTICATION
    path('dashboard/reservations/', views.reservation_list, name='reservation_list'),
    path('dashboard/reservations/add/', views.add_reservation, name='add_reservation'),
    path('dashboard/reservations/edit/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('dashboard/reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
    
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'), 


    path('dashboard/reservation/', views.create_reservation, name='create_reservation'),
    path('dashboard/reservation/success/', views.reservation_success, name='reservation_success'),
]





