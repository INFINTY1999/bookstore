from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    path('storeview/<str:pk>/', views.storeview, name="store"),
    path('storeadd/', views.storeadd, name="storeadd"),
    path('storeedit/<str:pk>/', views.storeedit, name="storeedit"),
    path('storeeditadd/<str:pk>/', views.storeeditadd, name="storeeditadd"),
    path('storedelete/<str:pk>/', views.storedelete, name="storedelete"),

    path('Bookview/<str:pk>/', views.bookview, name="bookview"),
    path('Bookadd/', views.bookadd, name="bookadd"),
    path('Bookedit/<str:pk>/', views.bookedit, name="bookedit"),
    path('Bookdelete/<str:pk>/', views.bookdelete, name="bookdelete"),
    
    path('login/', views.Login, name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registeruser,name="register"),
]
