from datetime import datetime
from django.conf.urls import url,include
from app.forms import BootstrapAuthenticationForm
from . import views


urlpatterns = [
    url(r'^$',views.home, name='home')
]
