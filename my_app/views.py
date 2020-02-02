from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')
