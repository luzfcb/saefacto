# -*- coding: utf8 -*-
from django.conf.urls import patterns, include, url
from .views import HomeView, AboutView

urlpatterns = patterns('',
                       url(r'^$',
                           HomeView.as_view(),
                           name="home"),
                       url(r'^about/$',
                           AboutView.as_view(),
                           name="about"),
    url(r'^ajax/notify/mail/$', 'main.views.mail', name='mail_ajax'),
    url(r'^ajax/notify/notifications/$', 'main.views.notifications', name='notification_ajax'),
    url(r'^ajax/notify/tasks/$', 'main.views.task', name='task_ajax'),
)
