from django.shortcuts import render
import requests

def home(request):
    response = requests.get('http://api.ipstack.com/check?access_key=28801c5ccfc535b3216e1f6c335022d9')
    geodata = response.json()
    return render(request, 'home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'city': geodata['city']
    })

    # return render(request, 'home.html')
