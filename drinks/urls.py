"""
URL configuration for drinks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", views.drink_list),  # List of all drinks
    path("api/<int:id>", views.drink_info),  # Individual drink
    path("api/random/", views.random_drinks),  # List of random drinks
    path("api/search/name", views.search_drink_name),  # Search for drinks by name
    path("api/search/ingredient", views.search_drink_ingredient),  # Search for drinks by ingredient
    path("", views.homepage, name="homepage"),
    path("account/", include("accounts.urls")),
    path("drinks/<int:id>", views.drink_detail, name="drink_detail"),
    path("drinks/", views.drinks, name="drinks"),
    # path("mocktails/<name>", views.mocktail_detail),
    path("account/create/", views.create, name="create"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin:password
