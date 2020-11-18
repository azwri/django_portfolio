from django.shortcuts import render
from .models import Job



def index(request):
    context = {
        'job': Job.objects.all()
    }
    return render(request, 'jobs/index.html', context)
