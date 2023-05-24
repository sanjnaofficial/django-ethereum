from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import requests

@csrf_exempt
def index(request):
    if request.method == 'POST':
        address = request.POST['address']
        response = requests.get('https://api.etherscan.io/api?module=account&action=balance&address=' + address + '&apikey=99YPF2ACMHC5HK21GSKNCFZQDFQDX7283Y')
        balance = response.json()['result']
        transactions = requests.get('https://api.etherscan.io/api?module=account&action=txlist&address=' + address + '&startblock=0&endblock=99999999&apikey=99YPF2ACMHC5HK21GSKNCFZQDFQDX7283Y').json()['result']
        recent_transactions = transactions[:5]  # Retrieve only the first 5 transactions
        return render(request, 'index.html', {'balance': balance, 'recent_transactions': recent_transactions})
    else:
        return render(request, 'index.html')

