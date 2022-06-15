from django.shortcuts import redirect, render, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

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
    return render(request, 'core/checkout.html')

@login_required
def payments_view(request):
    return render(request, 'core/payments.html')

@login_required
def services_view(request):
    return render(request, 'core/services.html')
