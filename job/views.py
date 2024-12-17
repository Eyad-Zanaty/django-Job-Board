from django.shortcuts import render
from .models import Job

# Create your views here.
def Job_type(request):
    jobs = Job.objects.all()
    context = {'jobs' : jobs}
    return render(request, 'job/job_type.html' , context)

def Job_details(request, id):
    job = Job.objects.get(id= id)
    context = {'job': job}
    return render(request, 'job/job_details.html', context)