from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    name = request.POST['name']
    amount = len(name.split())
    return render(request, 'counter.html', {'amount': amount})