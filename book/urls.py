"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from bokk.views import Home,login_view,signup_view,Children,Political,Poetry,ArtDesign,Programing
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
app_name='bokk'

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^Home/$',Home,name='Home'),
    url(r'^login/$',login_view,name='login_view'),
    url(r'^signup/$',signup_view,name='signup_view'),
    url(r'^Children/$',Children,name='Children'),
    url(r'^Political/$',Political,name='Political'),
    url(r'^Poetry/$',Poetry,name='Poetry'),
    url(r'^ArtDesign/$',ArtDesign,name='ArtDesign'),
    url(r'^Programing/$',Programing,name='Programing'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

