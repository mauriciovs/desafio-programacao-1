# -*- coding: utf-8 -*-
"""
Arquivo de urls principais.
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'^', include('sales.sales_manager.urls',
                      namespace='sales_manager',
                      app_name='sales_manager')),

    (r'^admin/', include(admin.site.urls)),

)
