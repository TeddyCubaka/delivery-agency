# from django.conf.urls import url
from django.urls import path, include
from . import views
from user import urls as user_urls

urlpatterns = [
    path('address', views.AddressView.as_view()),
    path('address/ville', views.VilleView.as_view(), name='ville'),
    path('address/province', views.ProvinceView.as_view(), name='province'),
    path('user/', include(user_urls))
]