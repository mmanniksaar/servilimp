from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('category/<slug:category_slug>/', views.rental_view, name='products_by_category'),

    path('', views.rental_view, name='rental'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

]

