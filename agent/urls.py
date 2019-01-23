"""agent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agent/', views.agent1),
    path('contacts/', views.agent2),
    path('location/', views.agent3),
    path('address/', views.agent4),
    path('form/', views.form),
    path('form1/', views.form1),
    path('form2/', views.form2),
    path('form3/', views.form3),
    path('form4/', views.form4),
    path('form5/', views.form5),
    path('form6/', views.form6),
    path('form7/', views.form7),
    path('', views.agent5),
    path("vasanth/",views.record1),
    path("records2/",views.record2),
    path("records3/",views.record3),
    path("records4/",views.record4),
    path("regs/",views.regs),
    path("reg/",views.reg),
    path("login/",views.login),
]
