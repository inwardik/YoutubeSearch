import pprint
import json

from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponse
from .video import get_videos_links, get_video_stat


def main_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            params = form.cleaned_data
            content = get_videos_links(params)
            pprint.pprint(params)
            return render(request, 'Youtube/index_search.html', {'form': form, 'content': content})
        else:
            return render(request, 'Youtube/index_search.html', {'form': form})
    else:
        form = SearchForm()
        return render(request, 'Youtube/index_search.html', {'form': form})


def detail(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        res = get_video_stat(q)
        return HttpResponse(json.dumps(res))