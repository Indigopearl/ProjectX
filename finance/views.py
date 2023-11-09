# finance/views.py
import os
from decouple import config
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def finnhub_webhook(request):
    # Example: Fetch data from Finnhub API
    finnhub_api_key = os.getenv("FINNHUB_API_KEY")
    symbol = "AAPL"  # Example symbol (Apple Inc.)
    api_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={finnhub_api_key}"

    try:
        response = requests.get(api_url)
        data = response.json()
        # Process the data as needed
        return render(request, "webhook_data.html", {"symbol": symbol, "data": data})
    except requests.exceptions.RequestException as e:
        return JsonResponse(
            {"error": f"Error fetching data from Finnhub API: {str(e)}"}, status=500
        )
