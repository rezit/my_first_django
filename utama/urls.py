from django.conf.urls import url
from django.contrib import admin
from  utama import views

urlpatterns = [
    url(r'^$', views.beranda, name='beranda'),
    url(r'^quran/$', views.quran, name='quran'),
    url(r'^quran/arrayyan/$', views.arrayyan, name='arrayyan'),
    url(r'^quran/fasya/$', views.fasya, name='fasya'),
    url(r'^pembelian/$', views.pembelian, name='pembelian'),
    url(r'^form_action/$', views.form_action, name='form_action'),
]