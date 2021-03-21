from django.urls import path
from .views import AddToWallet

urlpatterns = [
    path('add-to-wallet/', AddToWallet.as_view(), name='add-to-wallet'),
]