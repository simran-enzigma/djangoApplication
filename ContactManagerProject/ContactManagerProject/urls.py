"""
Definition of urls for ContactManagerProject.
"""

from datetime import datetime
from django.conf.urls import url,include
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^', include('ContactManagerApp.urls'), name='Apphome'),
    ]
