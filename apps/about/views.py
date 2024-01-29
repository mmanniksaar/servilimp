from django.shortcuts import render
from apps.about.models import About

# Create your views here.
def about_view(request):
    about_items = About.objects.all()
    print(about_items)
    if not about_items:
        print("No about objects found.")
    context = {'about_items': about_items}
    return render(request, 'about.html', context)