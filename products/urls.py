from django.urls import path
from . import views

# /products
# /products/1/detail therefore '' = root

urlpatterns = [
    path('', views.index),
    path('new', views.productpage)
]

