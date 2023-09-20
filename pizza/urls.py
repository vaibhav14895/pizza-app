"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login_page,name="login"),
    path('register/', views.register, name="register"),
    path('logout/',views.logout_page,name="logout"),
    path('addcart/<str:pizza_uid>/', views.addcart, name="addcart"),
    path('cart/',views.orderpage,name='cart'),
    path('removecartitem/<str:item_uid>',views.removeitem,name="removeitem"),
    path('payment/',views.payment,name="payment"),
    path('production/',views.production,name="production"),
    path('edit/<str:uid>',views.edit_pizza,name="editpizza"),
    path('delete/<str:uid>',views.delete_pizza,name="deletepizza"),
    path('add_pizza/',views.add_pizza,name="add_pizza"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
