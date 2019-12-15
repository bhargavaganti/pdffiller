"""pdffiller URL Configuration

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
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fam/add', views.fam_new),
    path('', views.fam_show),
    path('back', views.back),
    path('fam/edit/<int:id>', views.fam_edit),
    path('fam/update/<int:id>', views.fam_update),
    path('fam/update/<int:id>', views.fam_update),
    path('fam/print/<int:id>', views.fam_print),
    path('fam/delete/<int:id>', views.fam_destroy),
    path('ind/add', views.ind_new),
    path('ind/edit/<int:id>', views.ind_edit),
    path('ind/update/<int:id>', views.ind_update),
    path('ind/print/<int:id>', views.ind_print),
    path('ind/delete/<int:id>', views.ind_destroy),
]
