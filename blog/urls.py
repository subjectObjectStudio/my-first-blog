# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:39:22 2017

@author: subjectOBject

This file holds the Django URLS from the Django Girls tutorial
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list')
    ]