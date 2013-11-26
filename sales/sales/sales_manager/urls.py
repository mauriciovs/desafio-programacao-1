# -*- coding: utf-8 -*-
"""
URLs para a aplicação dos usuários
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('sales.sales_manager.views',

    url(r'^upload/$', view='upload',
                        name='upload'),

    url(r'^processar/$', view='processar',
                        name='processar'),
)
