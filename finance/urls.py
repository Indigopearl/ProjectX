# finance/urls.py
from django.urls import path
from .views import finnhub_webhook

urlpatterns = [
    path("your-webhook-endpoint/", finnhub_webhook, name="finnhub_webhook"),
    # Add other URL patterns as needed
]
