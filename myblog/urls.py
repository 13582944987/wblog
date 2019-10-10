from django.urls import path,include
from django.conf.urls import url
from myblog.views import *
# import xadmin
urlpatterns = [
    url(r'^$',index),
    url(r'^text-(\d+)', blog_content),
    url(r'^userinfor/',user_infor),
    url(r'^userfile/', user_file),
    url(r'^ueditor',include('DjangoUeditor.urls')),
]