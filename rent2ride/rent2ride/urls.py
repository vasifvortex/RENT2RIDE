"""
URL configuration for rent2ride project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from app import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('bikes/', views.bikes, name='bikes'),
    path('bike/<int:cycle_id>/', views.bike, name='bike'),
    path('favourites/', views.favourites_view, name='favourites'),
    path('api/read/', views.read),
    path('api/read_single/<int:cycle_id>/', views.read_single, name='read_single'),
    path('api/create/', views.create),
    path('api/update/<int:cycle_id>/', views.update),
    path('api/delete/<int:cycle_id>/', views.delete),
    path('registration/', views.register, name='registration'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('contact/', views.contact, name='contact'),
    # path("bill",views.order,name = "bill"),
    path('account/', views.account_view, name='account'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('cart.urls')),
]