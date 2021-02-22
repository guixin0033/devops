"""mysite URL Configuration

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
from django.urls import path,include
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('moni/',include('monitor.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# urlpatterns = [
#     url(r'^index/',views.index),
#     url(r'^admin/',admin.site.urls),
#     url(r'^$',views.home)
# ]

#
# urlpatterns = [
#     path('runoob/',views.runoob),
#     path('testdb/',testdb.testdb),
#     path('admin/',admin.site.urls)
# ]

# from django.conf.urls import include, url
# from django.contrib import admin
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^monitor/', include('monitor.urls')),
#     url(r'^', include('monitor.urls'))
# ]
