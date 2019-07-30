"""omniat URL Configuration

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
from core.views import *
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings # new
from django.conf.urls.static import static # new
from products.views import product_detail_view #mayDelete_it

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('social/', social_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('core/',include('core.urls')),
    path('product/', product_detail_view),


]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)