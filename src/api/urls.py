from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PostLikeAPIView,
    PostUpdaAPIView
    )

urlpatterns = [
    url(r'^post/$', PostUpdaAPIView.as_view({'get': 'list', 'post':'create'})),
    url(r'^post/(?P<pk>\d+)/$', PostUpdaAPIView.as_view({'get': 'retrieve', 'put':'update', 'delete': 'destroy'})),
    url(r'^post/(?P<pk>\d+)/like/$', PostLikeAPIView.as_view({'get': 'list', 'post':'create', 'delete': 'destroy'})),
]
urlpatterns = format_suffix_patterns(urlpatterns)
