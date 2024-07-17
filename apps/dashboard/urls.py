from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account/admin/', views.account_admin, name='account-admin'),
    path('account/customer/', views.account_customer, name='account-customer'),
    path('modify-customer', views.editar_usuario, name='editar-usuario'),
    path('account/admin/search-customer/<str:pk>/', views.buscar, name='search-customer'),
    path('account/admin/delete-customer/<str:pk>/', views.delete, name='delete-customer'),
]

