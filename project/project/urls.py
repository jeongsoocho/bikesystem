"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import bike.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bike.views.home, name='home'),
    path('rent/', bike.views.rent, name='rent'),
    path('rentbike',bike.views.rentbike, name='rentbike'),
    # path('rent/rentbike/rentsuccess',bike.views.rentsuccess, name='rentsuccess'),
    # path('returnbike/', bike.views.returnbike, name='returnbike'),
    # path('request/', bike.views.claim, name='request'),
    # path('request/requestsuccess/', bike.views.requestsuccess, name='requestsuccess'),
    # path('returnbike/payment/', bike.views.payment, name='payment'),
    # path('returnbike/payment/returnsuccess/', bike.views.returnsuccess, name='returnsuccess'),
]
