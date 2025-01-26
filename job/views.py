from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import ApplyForm, JobForm
from django.contrib.auth.decorators import login_required
from .filter import JobFilter

# Create your views here.
def Job_type(request):
    jobs = Job.objects.all()
    myfilter= JobFilter(request.GET,queryset=jobs)
    jobs= myfilter.qs
    paginator = Paginator(jobs, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj, 'myfilter': myfilter}
    return render(request, 'job/job_type.html' , context)

def Job_details(request, slug):
    job = Job.objects.get(slug= slug)
    if request.method== "POST":
        form = ApplyForm(request.POST ,request.FILES)
        print("Hello")
        if form.is_valid():
            myform= form.save(commit=False)
            myform.job= job
            myform.save()
    else:
        form= ApplyForm()
    context = {'job': job, 'form': form}
    return render(request, 'job/job_details.html', context)

@login_required
def apply_job(request):
    if request.method== "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform= form.save(commit= False)
            myform.owner= request.user
            myform.save()
            return redirect('jobs:job_list')
    else:
        form = JobForm(request.POST, request.FILES)
    context = {'form': form}
    return render(request, 'job/job_apply.html', context)