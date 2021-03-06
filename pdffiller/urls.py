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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('back', views.back),
    path('pdf', views.pdf),
    #Family Record URL's
    path('fam_show', views.fam_show),
    path('fam/add', views.fam_new),
    path('fam/edit/<int:id>', views.fam_edit),
    path('fam/update/<int:id>', views.fam_update),
    path('fam/paid/<int:id>', views.fam_paid),
    path('fam/print/<int:id>', views.fam_print),
    path('fam/delete/<int:id>', views.fam_destroy),
    ##Individual Record URL's
    path('ind_show', views.ind_show),
    path('ind/add', views.ind_new),
    path('ind/paid/<int:id>', views.ind_paid),
    path('ind/edit/<int:id>', views.ind_edit),
    path('ind/update/<int:id>', views.ind_update),
    path('ind/print/<int:id>', views.ind_print),
    path('ind/delete/<int:id>', views.ind_destroy),
]
