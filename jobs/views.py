from django.shortcuts import render,redirect
from .models import Jobs
# Create your views here.
def get_job_home(req):
    all_jobs=Jobs.objects.all()
    context={
        "all_jobs":all_jobs
    }
    return render(req,'jobs_home.html',context=context)

def get_add_jobs(req):
    if req.method=="GET":
        return render(req,'add_jobs.html')  
    else:   
        jobs_name=req.POST['jobs_name']
        jobs_description=req.POST['jobs_description']
        jobs_Title=req.POST['jobs_Title']
        location=req.POST['jobs_location']
        salary=req.POST['jobs_salary']
        jobs=Jobs(jobs_name=jobs_name,jobs_Title=jobs_Title,jobs_description=jobs_description,location=location,salary=salary)
        jobs.save()
        
        return redirect('jobs_home')

def get_update_jobs(req,ID):
    prev_job=Jobs.objects.get(id=ID)

    if req.method=="GET":
        context={
            "current_job":prev_job
        }
        return render(req,'update_jobs.html',context=context)  
    else:

        jobs_name=req.POST['jobs_name']
        jobs_description=req.POST['jobs_description']
        jobs_Title=req.POST['jobs_Title']
        location=req.POST['jobs_location']
        salary=req.POST['jobs_salary']
        
        prev_job.jobs_name=jobs_name
        prev_job.jobs_description=jobs_description
        prev_job.location=location
        prev_job.salary=salary
        prev_job.jobs_Title=jobs_Title
        
        return redirect('jobs_home')

def delete(req,ID):
    prev_job=Jobs.objects.get(id=ID)
    prev_job.delete()
    return redirect('jobs_home')
