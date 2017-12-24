from django.conf.urls import url
from . import views


app_name="webapp"

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'thankyou', views.saveuserdata, name="thankyou"),
url(r'index10', views.index10, name="index10")
]
