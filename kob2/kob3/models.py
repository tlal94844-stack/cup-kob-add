from django.db import models
from django.utils import timezone
# Create your models here.
CATEGORY_CHOICES = [
    ('electronics', 'إلكترونيات وأجهزة ذكية'),
    ('fashion', 'أزياء وموضة'),
    ('perfumes', 'عطور ومساحيق تجميل'),
    ('food', 'طعام وتوصيل وجبات'),
    ('travel', 'سفر وتجارة دولية'),
    ('home', 'العناية بالمنزل والمنتجات اليومية'),
    ('health', 'الصحة والرياضة'),]
class Cat(models.Model):
    name=models.CharField(max_length=100,verbose_name='اسم القسم')
    slug=models.SlugField(unique=True,verbose_name='رابط القسم(slug)')
    #يحول اسم القسم الئ نص انجليزي نظيف يستعمل في الرابط URL
    image = models.ImageField(upload_to='categories_images/', null=True, blank=True, verbose_name='شعار القسم')


    def __str__(self):
            return self.name

class Sto(models.Model):
    name = models.CharField(max_length=100, verbose_name='اسم المتجر')
    slug = models.SlugField(unique=True, verbose_name='رابط المتجر (Slug)')
    image = models.ImageField(upload_to='stores_images/', null=True, blank=True, verbose_name='شعار المتجر')
    link = models.URLField(verbose_name='رابط الموقع الرسمي')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')

    def __str__(self):
        return self.name
class Cou(models.Model):
    OFFER_TYPES=(
         ('coupon','كوبون خصم'),
         ('link','رابط عرض مباشر'),

    )
    store = models.ForeignKey(Sto, on_delete=models.CASCADE, related_name='coupons', verbose_name='المتجر التابع له')
    category=models.ForeignKey(Cat,on_delete=models.SET_NULL,null=True,blank=True,related_name='coupons',verbose_name='القسم')
    offer_type=models.CharField(max_length=100,choices=OFFER_TYPES,default='coupon',verbose_name='نوع العرض')
    title = models.CharField(max_length=200, verbose_name='عنوان العرض أو الخصم')
    code = models.CharField(max_length=50, blank=True, null=True,verbose_name='كود الخصم')
    discount_percentage = models.CharField(max_length=50, blank=True, null=True, verbose_name='نسبة أو قيمة الخصم')
    description = models.TextField(blank=True,null=True,verbose_name='تفاصيل الشروط أو الوصف')
    affiliate_link = models.URLField(blank=True, null=True,verbose_name='رابط الأفلييت المخصص')
    is_active = models.BooleanField(default=True, verbose_name='هل الكوبون فعال؟')
    expiry_date=models.DateTimeField(null=True,blank=True,verbose_name='تاريخ الانتهاء')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإضافة')

    def __str__(self):
        return f"{self.title} - ({self.code})"

    def is_coupon_active(self):
         if self.expiry_date:
              return timezone.now() <self.expiry_date
         return True
