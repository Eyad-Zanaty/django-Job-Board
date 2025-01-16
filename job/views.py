from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import ApplyForm, JobForm

# Create your views here.
def Job_type(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 4)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs' : page_obj}
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