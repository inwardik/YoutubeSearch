import pprint

from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm

from .video import get_videos_links


def main_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            params = form.cleaned_data
            content = get_videos_links(params, is_post=True)
            pprint.pprint(params)
            return render(request, 'Youtube/index_search.html', {'form': form, 'content': content})
        else:
            print("related")
    elif request.method == 'GET':
        form = SearchForm()
        params = request.GET
        content = get_videos_links(params, is_post=False)
        return render(request, 'Youtube/index_search.html', {'form': form, 'content': content})
    else:
        form = SearchForm()
    return render(request, 'Youtube/index_search.html', {'form': form})


def related_search(request):
    if request.method == 'GET':
        p = request.GET['related_video']
        print(p)
        params = []
        return HttpResponse('There is no get responces')
        content = get_videos_links(params)
    else:
        #return render(request, 'Youtube/index_search.html', {'content': content})
        pass
