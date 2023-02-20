from django.urls import path, include
from . import views

app_name = 'accounts'


urlpatterns = [
    path('request/', views.RequestView.as_view(), name='request'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
]

API_URL_SEND = 'https://pay.ir/pg/send'
# Bank payment page in which user enters his/her card information for payment.
API_URL_PAYMENT_GATEWAY = 'https://pay.ir/payment/gateway/{trans_id}'
# Verification and committing transactions endpoint.
API_URL_VERIFY = 'https://pay.ir/payment/verify'