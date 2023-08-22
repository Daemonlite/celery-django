from celery import shared_task
import requests
from decimal import Decimal
from .models import BTC
from prices.settings import REDIS

@shared_task
def fetch_btc_price():
    endpoint = "https://blockchain.info/tobtc?currency=USD&value=1"
    response = requests.get(endpoint)
    btc_price = Decimal(response.text)
    
    BTC.objects.create(fiat='USD', crypto=btc_price)
    REDIS.set('btc_price', int(btc_price))
    return f"BTC price fetched and cached: {btc_price}"


