# from django.conf.urls import url
from django.urls import path, include
from . import views
from user import urls as user_urls

urlpatterns = [
    path('address', views.AddressView.as_view()),
    path('address/city', views.CityView.as_view(), name='ville'),
    path('address/province', views.ProvinceView.as_view(), name='province'),
    path('address/country', views.CountryView.as_view(), name='country'),
    path('address/township', views.TownshipView.as_view(), name='country'),
    path('user/', include(user_urls))
]