from django.conf.urls import url
from . import views


app_name="webapp"

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'thankyou', views.saveuserdata, name="thankyou"),
url(r'index10', views.index10, name="index10"),
url(r'index11', views.index11, name="index11"),
url(r'index12', views.index12, name="index12")
]
