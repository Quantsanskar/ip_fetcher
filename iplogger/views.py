from django.shortcuts import render
from .models import IPAddress
from django.http import HttpRequest

def get_client_ip(request: HttpRequest):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def thank_you(request):
    ip = get_client_ip(request)
    IPAddress.objects.get_or_create(ip=ip)
    return render(request, 'ip/thankyou.html', {'ip': ip})

def show_all_ips(request):
    ips = IPAddress.objects.all().order_by('-timestamp')
    return render(request, 'ip/all_ips.html', {'ips': ips})