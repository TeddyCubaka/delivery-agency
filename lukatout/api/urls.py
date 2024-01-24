# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('address', views.AddressView.as_view()),
    path('address/ville', views.VilleView.as_view(), name='ville'),
    path('address/province', views.ProvinceView.as_view(), name='province'),
]