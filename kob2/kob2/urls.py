"""
URL configuration for kob2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
import json
def assetlinks_view(request):
    data = [{
      "relation": ["delegate_permission/common.handle_all_urls"],
      "target": {
        "namespace": "android_app",
        "package_name": "fit.couponbox.twa",
        "sha256_cert_fingerprints": ["0B:B9:F8:9A:BA:54:59:C4:2C:5D:22:CB:78:D6:89:5B:75:B3:2E:E4:06:94:45:B2:F0:36:DE:D7:EE:CE:4E:0F"]
      }
    }]
    return HttpResponse(json.dumps(data), content_type="application/json")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kob3.urls')),
    path('.well-known/assetlinks.json', assetlinks_view),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
