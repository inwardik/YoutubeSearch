from django.shortcuts import render


def inw(request):
    return render(request, 'inw/index.html')
