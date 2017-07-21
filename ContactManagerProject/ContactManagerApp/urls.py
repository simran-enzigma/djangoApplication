from datetime import datetime
from django.conf.urls import url,include
from app.forms import BootstrapAuthenticationForm
from . import views


urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^EditContact/(?P<SerialNo>[0-9]+)$',views.EditContact, name='EditContact'),
    url(r'^AddContact/$',views.AddContact, name='AddContact'),
    url(r'^DeleteContact/(?P<SerialNo>[0-9]+)$',views.DeleteContact, name='DeleteContact'),
    url(r'^searchContact/(?P<search>[a-zA-Z]+)$',views.searchContact, name='searchContact'),
 ]