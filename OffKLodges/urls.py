from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import LodgeDetailView, ConfPayment, Lodge_booking
from django.conf.urls import url
import notifications.urls

urlpatterns = [
    path('', views.index, name='index'),
    path('findroomateconfirm/', views.roommateResult, name='findroomateconfirm'),

    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name= 'logout'),
    path('register/', views.register, name= 'register'),
    path('profile/', views.profile, name='profile'),
    #path('booked/', views.booked, name='booked'),
    #path('all_lodges/', views.allLodges, name='all_lodges'),

    path('lodge_detail/<int:pk>/', LodgeDetailView.as_view(), name= 'lodge_detail'),

    url('search/', views.search, name='search'),
    url('filters/', views.filter, name='filters'),

    
    
    #path("terms", views.KeywordListView.as_view(),name="terms"),
    #path("terms/<int:page>", views.listing, name="terms-by-page"),
    path("terms.json", views.listing_api, name="terms-api"),
    path("list", views.listing, name='list'),

    #path("findroomate", views.findRoomie, name='findroomate'),
    #url('search/', views.search, name='search'),

    #path('booking/', views.bookings, name='booking'),
    path('booking/<int:id>/', views.bookings, name='booking'),
    path('message/', views.message, name='message'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),

    path('Personal_Info/', views.agentPersonalInfo, name='agentPersonalInfo'),
    path('agent_Properties/', views.agentProperties, name='agentProperties'),

    path('ini_pay/<int:id>/', views.ini_pay, name='ini_pay'),
    #path('confirm_payment', views.deposit, name='confirm_payment'),
    path('confirm_payment/<int:pk>/', ConfPayment.as_view(), name= 'confirm_payment'),
    url('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('<str:ref>/', views.verify_payment, name='verify-payment'),
    
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
