# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Erik van Widenfelt
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from edc_bootstrap.views import LoginView, LogoutView, HomeView

admin.autodiscover()

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='login_url'),
    url(r'^logout/', LogoutView.as_view(url='/'), name='logout_url'),
    url(r'^accounts/login/', LoginView.as_view()),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', HomeView.as_view(), name='home'),
]
