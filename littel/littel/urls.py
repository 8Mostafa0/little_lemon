
from django.contrib import admin
from django.urls import path,include
from menu import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("details/",views.about,name="about"),
    path("uploads/<str:file>",views.upload),
    path("menu/",include('menu.urls'))
]
