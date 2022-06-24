from django.urls import path
from . import views
from django.contrib import admin

app_name = 'core'

admin.site.site_header = 'SuperGym'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('panel', views.panel, name='panel'),
    path('client/panel/', views.client_panel_view, name='client_panel'),
    path('client/panel/payments/checkout', views.checkout_view, name='checkout'),
    path('client/panel/payments', views.payments_view, name='payments'),
    path('client/panel/secrvices', views.services_view, name='services'),
    path('client/requests/service/add/<int:id>', views.add_service, name='add_service'),
    path('client/requests/service/checkout', views.checkout_pay, name='checkout_pay'),
    path('staff/panel/', views.staff_panel_view, name='staff_panel')
]
