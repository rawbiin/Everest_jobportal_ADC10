from django.urls import path
from .views import *

urlpatterns = [
 path('',get_job_home,name="jobs_home"),
 path('add_jobs',get_add_jobs),
 path('update_jobs',get_update_jobs),
 

]

