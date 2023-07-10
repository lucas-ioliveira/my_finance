from django.urls import path
from .views import DashViews, ProfileViews, HelpCenterViews
from .views import SettingViews, TransationDetailViews, WalletViews

urlpatterns = [
    path('', DashViews.as_view(), name='dash'),
    path('profile/', ProfileViews.as_view(), name='profile'),
    path('help/', HelpCenterViews.as_view(), name='help'),
    path('setting/', SettingViews.as_view(), name='setting'),
    path('transation/', TransationDetailViews.as_view(), name='transation'),
    path('wallet/', WalletViews.as_view(), name='wallet'),
]