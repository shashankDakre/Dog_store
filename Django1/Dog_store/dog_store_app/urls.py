from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/',views.cart,name="cart"),
    path('add/',views.add,name="add"),
    path('read/',views.read,name="read"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete"),
]