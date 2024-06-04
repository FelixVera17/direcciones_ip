from django.shortcuts import render, redirect
from .models import User, MacAddress

def index(request):
    return render(request, 'index.html')

def register_ip(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        user_name = request.POST.get('user_name')
        user_fullname = request.POST.get('user_fullname')

        user, created = User.objects.get_or_create(
            username=user_name,
            defaults={'name': user_fullname}
        )

        mac_address = MacAddress(ip_address=ip_address, id_user=user)
        mac_address.save()
        return redirect('index')

    return render(request, 'register_ip.html')

def search_ip(request):
    user_name= request.GET.get('user_name')
    if user_name:
        mac_addresses = MacAddress.objects.filter(id_user__username__icontains=user_name)
    else:
        mac_addresses = mac_addresses = MacAddress.objects.all()
    
    return render(request, 'search_ip.html', {'mac_addresses': mac_addresses})



