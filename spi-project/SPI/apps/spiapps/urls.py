from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'summ$', views.summ),
    url(r'inputData$', views.inputData),
    url(r'brows$', views.brows),
    url(r'pn$', views.pn),
    url(r'desc$', views.desc),
    url(r'bulk$', views.bulk),
    url(r'uploadData$', views.uploadData),
    url(r'bulksearch', views.bulksearch),
    # url(r'show', views.show),
    
]