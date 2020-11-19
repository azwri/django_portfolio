from django.shortcuts import render, get_object_or_404
from .models import Job



def index(request):
    queryset = Job.objects.all()   
    context = {
        'object_list': queryset
    }
    return render(request, 'jobs/index.html', context)

def detail(request, id):
    obj = get_object_or_404(Job, id=id)
    context = {
        'object': obj
    }
    return render(request, 'jobs/detail.html', context)
