from django.urls import path
from .views import PaymentCreateView, PayPalExecuteView, PaymentHistoryView, PayPalCancelView

urlpatterns = [
    path('create-payment/', PaymentCreateView.as_view(), name='create-payment'),
    path('paypalexecute-payment/', PayPalExecuteView.as_view(), name='execute-payment'),
    path('cancel-payment/', PaymentHistoryView.as_view(), name='cancelpayment'),
    path('cancel-payment/', PayPalCancelView.as_view(), name='cancel-payment'),
]
