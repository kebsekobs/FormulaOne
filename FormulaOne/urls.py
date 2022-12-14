"""kebseDjango URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import FormulaOne.admin as view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/<str:team>/', view.drivers_link),
    path('', view.home_link),
    path('points/', view.points_link),
    path('schedule/', view.schedule_link),
    path('login/', view.LoginUser.as_view(), name='login'),
    path('signin/', view.RegisterUser.as_view(), name='register'),
    path('logout/', view.logout_user, name='logout'),
    path('profile/', view.Profile.as_view(), name='profile'),
    path('shop/', view.shop, name='shop'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
