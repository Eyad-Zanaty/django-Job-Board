from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import ApplyForm

# Create your views here.
def Job_type(request):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 1)  # Show 25 contacts per page.
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