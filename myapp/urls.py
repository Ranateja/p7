from django.urls import path
from myapp import views
app_name='myapp'

urlpatterns= [
    path('child/',views.child,name='child'),
    path('home',views.home,name='home'),


]