from django.contrib import admin
from django.urls import path,include

from .views import test, TestListView


urlpatterns = [
    path('test/',test,name='test'),
    path('models/',TestListView.as_view(),name='test_models_url')
]
