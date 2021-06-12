from django.shortcuts import render
import json
from .phone import get_coords

API_KEY = 'AIzaSyAmVfqK9tJKNKcV9ochOOSetUyb_cGKo6Y&callback=initMap&libraries='

def index(request):
    if request.method == 'GET':
        if 'phone' in request.GET:
            phone_num = request.GET.get('phone')
            py_data = get_coords(phone_num)
            print(py_data)
            if py_data:
                return render(request, 'phoneinspace/index.html', {'py_data': json.dumps(py_data),
                                                                   'py_data_dict': py_data,
                                                                   'api': API_KEY})
        return render(request, 'phoneinspace/index.html')
