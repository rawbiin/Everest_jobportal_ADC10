from django.shortcuts import render,redirect
from .models import Jobs
# Create your views here.
def get_job_home(req):
    return render(req,'jobs_home.html')

def get_add_jobs(req):
    if req.method=="GET":
        return render(req,'add_jobs.html')  
    else:   
        jobs_name=req.POST['jobs_name']
        jobs_description=req.POST['jobs_description']
        location=req.POST['jobs_location']
        salary=req.POST['jobs_salary']
        jobs=Jobs(jobs_name=jobs_name,jobs_description=jobs_description,location=location,salary=salary)
        jobs.save()
        
        return redirect('jobs_home')

def get_update_jobs(req):
    return render(req,'update_jobs.html')    