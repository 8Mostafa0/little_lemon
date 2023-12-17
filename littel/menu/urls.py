from django.urls import path
from . import views
app_nane = "menuapp"
urlpatterns = [
    # path("",views.home,name="menu"),
    path("",views.MenuView.as_view(),name="menulist"),
    path("uploads/<str:file>",views.upload),
    path("<int:pk>/item/",views.SelectedItem.as_view(),name="selecteditem"),
]
