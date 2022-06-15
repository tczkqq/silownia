from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('panel', views.panel, name='panel'),
    path('client/panel/', views.client_panel_view, name='client_panel'),
    path('client/panel/payments/checkout', views.checkout_view, name='checkout'),
    path('client/panel/payments', views.payments_view, name='payments'),
    path('client/panel/secrvices', views.services_view, name='services'),
    path('staff/panel/', views.staff_panel_view, name='staff_panel')
]
