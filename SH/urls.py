
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index_view,name='index'),
    path('Aboutus/',views.Aboutus_view,name='Aboutus'),
    path('Beds/',views.Beds_view,name='Beds'),
    path('Tables/',views.Tables_view,name='Tables'),
    path('Sofas/',views.Sofas_view,name='Sofas'),
    path('cart/',views.cart_view,name='cart'),
     path('payment/',views.payment_view,name='payment'),
    path('contact/',views.contact_view,name='contact'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup_view,name='signup'),
    path('',views.home_view,name='home'),
]