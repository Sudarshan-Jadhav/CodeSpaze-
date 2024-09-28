import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def scrape(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        
      
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        titles = soup.find_all('h1')  # Scraping all <h1> tags as an example

        titles_text = [title.get_text() for title in titles]
        
        return render(request, 'results.html', {'titles': titles_text})
