from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from . import views
urlpatterns=[
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("register",views.register,name='register'),
    path("login/",LoginView.as_view(template_name='loginform.html'),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("change",views.change,name="change"),
    path("ques",views.ques,name='ques'),
    path("add",views.add,name="add"),
    path('user',views.user,name='user'),
   ]