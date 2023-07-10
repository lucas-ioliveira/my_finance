from django.urls import path
from .views import DashViews

urlpatterns = [
    path('', DashViews.as_view(), name='dash'),
]