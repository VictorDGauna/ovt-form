from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getIndex, name='index'),
    path('success', views.save_form, name='success'),
]
