from django.shortcuts import render
from .models import Port


# Create your views here.


def index(request):
    """
    dest1 = Port()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city that never sleeps'
    dest1.capacity = 700
    dest1.img = 'destination_1.jpg'
    dest1.offer = False
    dest1.annualtraffic = 0

    dest2 = Port()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.capacity = 650
    dest2.offer = True

    dest3 = Port()
    dest3.name = 'Bangalore'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg' 
    dest3.capacity =  750
    dest3.offer = False
    """
    dests = Port.objects.all()

    #dests = [dest1, dest2, dest3]
    return render(request, "index.html", {'dests': dests})

def syndyasmenes(request):
    return render(request, "syndyasmenes.html")