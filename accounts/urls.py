from django.urls import path
from . import views
urlpatterns = [
    path("register",views.register,name="register"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("driver/",views.driver_pannel,name="driver_pannel"),
    path("rider/",views.rider_pannel,name="rider_pannel"),
    path("login/",views.user_login,name="login"),
    path("logout/",views.user_logout,name="logout"),


]
