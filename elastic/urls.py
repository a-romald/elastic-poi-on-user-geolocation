from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='main_index'),
    url(r'^poi/$', PoiRequest.as_view(), name='main_poi'),
    url(r'^get_draged/$', DragPoi.as_view(), name='main_draged'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
