from django.shortcuts import render, redirect 
from .models import User, MacAddress

def index(request):
    return render(request, 'index.html') 

def register_ip(request):
    if request.method == 'POST':
        ip_addres = request.POST.get('ip_addres')
        user_id = request.POST.get('user_id')
        mac_address = MacAddress(ip_addres= ip_addres, id_user_id =user_id)
        mac_address.save()
        return redirect('index')
    return render(request, 'register_ip.html')
def search_ip(request):
    mac_addresess = MacAddress.objects.all()
    return render (request, 'search_ip.html', {'mac_addresses': mac_addresess})


