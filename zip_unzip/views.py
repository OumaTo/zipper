from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'zip_unzip/index.html')

def zip(request):
    
    # path = request.Method.GET.get('path_zip')
    print(request.method)