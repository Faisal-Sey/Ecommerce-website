"""my_app URL Configuration

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
from django.urls import include, path

urlpatterns = [
    path('remove-total-from-cart/<slug>', include('blog.urls')),
    path('add-item-to-cart/<slug>', include('blog.urls')),
    path('remove-item-from-cart/<slug>', include('blog.urls')),
    path('order-summary', include('blog.urls')),
    path('remove-from-cart/<slug>', include('blog.urls')),
    path('add-to-cart/<slug>', include('blog.urls')),
    path('shop-details/<slug>', include('blog.urls')),
    path('add_to_cart', include('blog.urls')),
    path('posts_list', include('blog.urls')),
    path('Signup', include('blog.urls')),
    path('login', include('blog.urls')),
    path('Shorts', include('blog.urls')),
    path('Shirts', include('blog.urls')),
    path('Slippers', include('blog.urls')),
    path('Watches', include('blog.urls')),
    path('Pants', include('blog.urls')),
    path('Shoes', include('blog.urls')),
    path('shoping-cart', include('blog.urls')),
    path('blog', include('blog.urls')),
    path('index', include('blog.urls')),
    path('blog-details', include('blog.urls')),
    path('payment/<payment_option>', include('blog.urls')),
    path('checkout', include('blog.urls')),
    path('contact', include('blog.urls')),
    path('shop-grid', include('blog.urls')),
    path('', include('blog.urls')),
    path('posts', include('blog.urls')),
    path('postsforms', include('blog.urls')),
    path('answers', include('blog.urls')),
    path('admin/', admin.site.urls),
]
