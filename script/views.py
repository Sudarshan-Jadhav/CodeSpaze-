from django.shortcuts import render, redirect
from .models import ScriptedData
from .forms import ScriptForm
from bs4 import BeautifulSoup
import requests

def script_data(request):
    if request.method == 'POST':
        form = ScriptForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: Scraping the title and content of the first paragraph
            title = soup.title.string if soup.title else 'No Title'
            content = soup.find('p').get_text() if soup.find('p') else 'No Content'

            # Save the scraped data
            scraped_data = ScriptedData(url=url, title=title, content=content)
            scraped_data.save()

            return redirect('data_list')
    else:
        form = ScriptForm()

    return render(request, 'script/script.html', {'form': form})

def data_list(request):
    data = ScriptedData.objects.all().order_by('-scripted_at')
    return render(request, 'script/data_list.html', {'data': data})
