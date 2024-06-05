from django.shortcuts import render, redirect, get_object_or_404
from .models import User, MacAddress
from django.utils import timezone
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

        mac_address = MacAddress(ip_address=ip_address, id_user=user,date_registered=timezone.now())
        mac_address.save()
        return redirect('index')

    return render(request, 'register_ip.html')

def search_ip(request):
    user_name= request.GET.get('user_name')
    if user_name:
        mac_addresses = MacAddress.objects.filter(id_user__username__icontains=user_name)
    else:
        mac_addresses = mac_addresses = MacAddress.objects.all()
        
    for direccion_mac in mac_addresses:
        if direccion_mac.ip_address.split('.')[2] == '0':
            direccion_mac.sucursal = 'matriz'
        elif direccion_mac.ip_address.split('.')[2] == '2':
            direccion_mac.sucursal = 'sucursal 2'  
        elif direccion_mac.ip_address.split('.')[2] == '3':
            direccion_mac.sucursal = 'sucursal 1'  
        elif direccion_mac.ip_address.split('.')[2] == '4':
            direccion_mac.sucursal = 'sucursal 3'
        else:
            direccion_mac.sucursal = 'N/A'
    return render(request, 'search_ip.html', {'mac_addresses': mac_addresses})
def edit_ip(request, mac_id):
    mac_address = get_object_or_404(MacAddress, id=mac_id)
    if request.method == 'POST':
        ip_address = request.POST.get('ip_address')
        user_name = request.POST.get('user_name')
        user_fullname = request.POST.get('user_fullname')

        user, created= User.objects.get_or_create(
            username= user_name,
            defaults= {'name': user_fullname}
        )
        mac_address.ip_address = ip_address
        mac_address.id_user = user
        mac_address.save()
        return redirect ('search_ip')
    return render (request, 'edit_ip.html',{'mac_address': mac_address})

