from django.shortcuts import render
from .models import Tool

def home(request):
    tools = Tool.objects.all()
    return render(request, 'home.html',{'tools':tools})

# def tools(request):
#     tools = Tool.objects.all()
#     return render(request, 'tools.html', {'tools': tools})
