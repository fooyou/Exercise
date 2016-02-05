from django.conf.urls import url, patterns
from .views import archive

urlpatterns = patterns('',
    url(r'^$', archive)
)
