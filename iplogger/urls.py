from django.urls import path
from . import views

urlpatterns = [
    path('', views.thank_you, name='thank_you'),
    path('address/hbfhbeh/ejfbj/jbf/', views.show_all_ips, name='all_ips'),
]