from django.conf.urls import url

from .views import homepage

from .views import post_list

urlpatterns = [
    url(r'^post/list$', post_list),
    url(r'^', homepage)

]
