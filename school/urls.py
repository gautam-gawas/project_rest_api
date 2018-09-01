from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView

# router = DefaultRouter()
# router.register('projects', views.ProjectViewSet)
# router.register('users', views.UserViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path(r'^(?P<template_name>\w+)$', SimpleStaticView.as_view(), name='example'),
    # path(r'^$', TemplateView.as_view(template_name='index.html')),
    # path('', include(router.urls)),
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>/', views.ProjectDetail.as_view()),
    path('form/', views.FormList.as_view()),
    path('form/<int:pk>/', views.FormDetail.as_view()),
]
