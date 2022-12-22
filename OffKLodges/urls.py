from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import LodgeDetailView, ConfPayment
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('register/', views.register, name= 'register'),
    path('profile/', views.profile, name='profile'),
    path('booked/', views.booked, name='booked'),
    path('all_lodges/', views.allLodges, name='all_lodges'),

    path('lodge_detail/<int:pk>/', LodgeDetailView.as_view(), name= 'lodge_detail'),

    url('search/', views.search, name='search'),

    url('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),
    path('confirm_payment', views.deposit, name='confirm_payment'),
    path('confirm_payment/<int:pk>/', ConfPayment.as_view(), name= 'confirm_payment'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
