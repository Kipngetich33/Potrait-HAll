from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^all/',views.index, name= 'all'),
    url(r'^categories/(\d+)',views.categories,name = 'categories'),
    url(r'^details/(\d+)',views.details,name = 'details'),
    url(r'^search/',views.search, name= 'search')            

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)