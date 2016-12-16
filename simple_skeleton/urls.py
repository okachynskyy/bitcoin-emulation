from django.conf.urls import include, url
from django.contrib import admin

from simple_skeleton.apps.core import views as core_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', core_views.loginview),
    url(r'^logout/', core_views.logoutview),
    url(r'^message/', core_views.message),   
    url(r'^auth/', core_views.auth_and_login),
    url(r'^signup/', core_views.sign_up_in),
    url(r'^$', core_views.secured)
]