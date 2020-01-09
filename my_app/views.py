from django.shortcuts import render, get_object_or_404
from .models import Job


# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'my_app/homepage.html', {'jobs': jobs})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'my_app/details.html', {'job': job_detail})
