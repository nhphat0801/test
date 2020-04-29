from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('herb/', views.herbview, name='herbview'),
    path('herb/<int:herb_id>/', views.detailherb, name='detailherb'),
    path('compound/', views.compoundview, name='compoundview'),
    path('compound/<int:compound_id>/', views.detailcompound, name='detailcompound'),
    path('target/', views.targetview, name='targetview'),
    path('target/<int:target_id>/', views.detailtarget, name='detailtarget'),
    path('disease/', views.diseaseview, name='diseaseview'),
    path('query/', views.querycansmiles.as_view(), name='querycansmiles')
]