from django.shortcuts import render, get_object_or_404
from .models import Client

def clients_view(request):
    clients_items = Client.objects.all()
    if not clients_items:
        print("No client objects found.")
    context = {'clients_items': clients_items}
    return render(request, 'clients.html', context)
