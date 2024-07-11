from django.contrib import admin
from django.urls import path
from U_downlaoder import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),

]