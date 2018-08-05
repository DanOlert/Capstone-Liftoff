
from django.contrib import admin
from django.urls import path, include
from . import views
#NOTE when importing things with same name, you can use "as" to import as a different name
from posts import views as post_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#These are used for media import, NOTE: Pillow-5.2.0 has been installed
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('user/', include('user.urls')),
    path('apis/', include('apis.urls')),
    path('about/', views.about),
    #NOTE now root renders post_list
    path('', post_views.post_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns() #for assets like logos and css

#NOTE media import. may or may not use:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for media files users upload
