# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from django.conf.urls.defaults import patterns, url

from oneanddone.base import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='base.home'),
)
