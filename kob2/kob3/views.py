from django.shortcuts import render,get_object_or_404,redirect
from .models import Sto,Cou,Cat
# Create your views here.
from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Cat, Cou
from django.contrib import messages
import csv
from django.utils.text import slugify
from django.utils.dateparse import parse_datetime
import re
def k1(request):
    # استقبال فلاتر البحث، الأقسام، ونوع العرض
    category_id = request.GET.get('category')
    type_offer = request.GET.get('type_offer')
    search_query = request.GET.get('q', '').strip()  # استقلال كلمة البحث وتنظيفها

    # جلب الأقسام والكوبونات الفعالة مبدئياً
    categories = Cat.objects.all()
    coupons = Cou.objects.filter(is_active=True)

    # فلترة حسب القسم إذا تم اختياره
    if category_id:
        coupons = coupons.filter(category_id=category_id)

    # فلترة حسب نوع العرض إذا تم اختياره
    if type_offer:
        coupons = coupons.filter(offer_type=type_offer)

    # فلترة حصرياً باسم المتجر أو عنوان العرض بناءً على ما يكتبه المستخدم في البحث
    if search_query:
        coupons = coupons.filter(
            Q(store__name__icontains=search_query) | 
            Q(title__icontains=search_query)
        )

    context = {
        'coupons': coupons,
        'type_offer': type_offer,
        'cat': categories,
        'category_id': category_id,
        'search_query': search_query,  # تمرير قيمة البحث للقالب عشان ما تختفي بعد البحث
    }
    
    return render(request, 'kob3/home.html', context)
def coupon_detail(request,pk):
    coupon=get_object_or_404(Cou, pk=pk)
    context={'coupon':coupon}
    return render(request,'kob3/coupon_detail.html',context)
def toa(request):
    return render(request,'kob3/toasl.html')
def nhn(request):
    return render(request,'kob3/nhn.html')





def clean_html(raw_html):
    pass

def upload_csv(request):
    pass