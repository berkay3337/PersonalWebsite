from django.shortcuts import render

def aboutme_view(request):
    return render(request, 'aboutme.html', {})
