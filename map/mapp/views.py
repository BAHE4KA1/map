from django.shortcuts import render
from .models import *

def analitics(request):
    return render(request, 'mapp/analitika.html')

def home(request):
    return render(request, 'mapp/home.html')

def requ(request):
    logs = Log.objects.all()
    return render(request, 'mapp/requests.html', {'logs': logs})

def map(request):
    req = ''
    streets = Streets.objects.all()
    if request.method == 'POST':
        search = request.POST.get('search')
        if search != '':
            streets = Streets.objects.filter(name__icontains=search)
            try: req = str(streets[0].name)
            except: req = 'г. Краснодар'
        else:
            streets = Streets.objects.all()
            req = ''
    return render(request, 'mapp/map.html', {'streets': streets.order_by('-traffic_value'), 'req': req})