from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from .models import PaymentMethods, Payments, Service, UserService

def home_view(request):
    return render(request, 'core/home.html')





def panel(request):
    '''Redirects to correct panel'''    
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('core:staff_panel')
        
        return redirect('core:client_panel')
    
    return redirect('core:home')
    

@staff_member_required
def staff_panel_view(request):
    context = {}
    return render(request, 'core/staff_panel.html', context)

@login_required
def client_panel_view(request):
    context = {
        'user': request.user
    }
    return render(request, 'core/client_panel.html', context)


@login_required
def checkout_view(request):
    services = UserService.objects.filter(client=request.user, active=False)
    payments = PaymentMethods.objects.all()
    total = 0
    for s in services:
        total += s.service.price

    context = {
        'services': services,
        'total': total,
        'payments': payments
    }
    return render(request, 'core/checkout.html', context)

@login_required()
def checkout_pay(request):
    services = UserService.objects.filter(client=request.user, active=False)
    total = 0
    for s in services:
        total += s.service.price
    UserService.objects.filter(
        client=request.user).update(active=True)
    
    Payments.objects.create(
        client=request.user,
        method_id=3,
        to_pay = total,
        payed = total,
        realized = True
        
    )
    return redirect('core:payments')

@login_required
def payments_view(request):
    services = UserService.objects.filter(client=request.user, active=False)
    payments = Payments.objects.filter(client=request.user)
    total = 0
    for s in services:
        total += s.service.price

    context = {
        'services': services,
        'total': total,
        'payments': payments
    }
    return render(request, 'core/payments.html', context)

@login_required
def services_view(request):
    services = Service.objects.all()
    
    context = {
        'services': services
    }
    return render(request, 'core/services.html', context)

@login_required
def add_service(request, id):
    service = UserService.objects.create(client=request.user,service_id=id, active=False)
    return redirect('core:payments')
    
