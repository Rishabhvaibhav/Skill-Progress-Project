import requests
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if 'query' in request.GET:
        query = request.GET['query']
        proxies = {
            'http': '64.189.106.6:3129',
            'https': '64.189.106.6:3129',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        }
        response = requests.get(f'https://www.google.com/search?q={query}', proxies=proxies, headers=headers)
        return HttpResponse(response.text)
    return render(request, 'home.html')

