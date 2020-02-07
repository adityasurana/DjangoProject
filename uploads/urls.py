from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from uploads.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^external', views.external),
    url(r'^internal', views.internal),
    url(r'^twitter_tool/$', views.twitter_tool, name='twitter_tool'),
    url(r'^tweet_upload', views.tweet_upload),
    url(r'^tweet', views.tweet),
    url(r'^$', views.home, name='home'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)