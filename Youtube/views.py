import pprint

from django.shortcuts import render
from .forms import SearchForm

from .video import get_videos_links


def main_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            params = form.cleaned_data
            content = get_videos_links(params)
            pprint.pprint(params)
            return render(request, 'Youtube/index_search.html', {'form': form, 'content': content})
    else:
        form = SearchForm()
    return render(request, 'Youtube/index_search.html', {'form': form})
