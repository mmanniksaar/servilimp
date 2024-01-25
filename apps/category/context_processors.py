from apps.category.models import Category


# menu_links included in settings.py TEMPLATES section (now its function value is available every page)
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)