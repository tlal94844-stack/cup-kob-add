from django.urls import path
from .views import k1,coupon_detail,toa,nhn
urlpatterns = [
    path('',k1,name='k1'),
    path('coupon/<int:pk>/',coupon_detail,name='coupon_detail'),
    path('toa',toa,name='toa'),
    path('nhn',nhn,name='nhn'),
    #path('admin-upload-csv/', upload_csv, name='upload_csv'),

]
