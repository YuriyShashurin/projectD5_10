"""pets_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pets import views
from django.conf.urls.static import static
from django.conf import settings

handler404 = views.handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PetsListView.as_view(), name='index'),
    path('pets/koty/', views.CatListView.as_view(), name='cats'),
    path('pets/sobaki/', views.DogListView.as_view(), name='cats'),
    path('pets/popugai/', views.ParrotListView.as_view(), name='popugay'),
    path('pets/<int:pk>', views.PetInfoView.as_view(), name='pet_info'),
    path('pets/add_like/', views.add_like),
    path('blog/', views.BlogLisView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog'),
    path('aboutus/', views.ContactsPageView.as_view(), name='contacts'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)