"""patients URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.etree.ElementInclude import include
from App import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path to access the admin page
    path('admin/', admin.site.urls),
    # path to render homepage
    path('',views.frontend,name="frontend"),
    # path login/logout
    path('login/',include('django.contrib.auth.urls')),


    # backend
    path('backend/',views.backend,name="backend"),

    #path to add
    path('add_client/',views.add_patient,name="add_client")
]
