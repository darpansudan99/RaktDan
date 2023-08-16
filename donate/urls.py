from django.urls import path


from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
   
    

    path("register/<str:option>", views.registerOption, name="registerOption"),
    path("profile/<str:name>", views.profile, name="profile"),
    path("requests/", views.requests, name="requests"),
    path("response/<int:id>", views.response, name="response"),
    path("bloodBank/<str:bank_name>", views.bank, name="bank"),

    path("filter/<str:city>", views.filter, name="filter"),
    path("getunits/<str:btype>", views.getunits, name="getunits"),

]