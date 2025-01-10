from django.shortcuts import render

def home(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio-details.html')

def services(request):
    return render(request,'service-details.html')

def starter (request):
    return render (request,'starter-page.html')