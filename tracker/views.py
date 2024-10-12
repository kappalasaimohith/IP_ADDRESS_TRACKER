import requests
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def track_ip(request):
    # Public IPv4 address
    ipv4_response = requests.get('https://api.ipify.org?format=json')
    ipv4 = ipv4_response.json()['ip']

    # Public IPv6 address
    ipv6_response = requests.get('https://api64.ipify.org?format=json')
    ipv6 = ipv6_response.json()['ip']

    # Geographical data using ipinfo for IPv4
    geo_response_ipv4 = requests.get(f'https://ipinfo.io/{ipv4}/json')
    geo_data_ipv4 = geo_response_ipv4.json()

    # Geographical data using ipinfo for IPv6
    geo_response_ipv6 = requests.get(f'https://ipinfo.io/{ipv6}/json')
    geo_data_ipv6 = geo_response_ipv6.json()

    data = {
        'public_ipv4': ipv4,
        'public_ipv6': ipv6,
        'geo_data_ipv4': geo_data_ipv4,
        'geo_data_ipv6': geo_data_ipv6
    }


    return JsonResponse(data)
