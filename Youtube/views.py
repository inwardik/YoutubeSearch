from django.shortcuts import render
from .forms import SearchForm


def main_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            content = ['content']  # TODO content
            return render(request, 'Youtube/index_search.html', {'content': content})
    else:
        form = SearchForm()

    return render(request, 'Youtube/index_search.html', {'form': form})
