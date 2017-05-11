from django.conf.urls import url

from .views import homepage

from .views import post_list, post_detail

urlpatterns = [
    url(r'^post/list$', post_list),
    url(r'^', homepage)
    url(r'^post/(?P<id>[0-9]+)',post_detail, name="post-detail")

]
