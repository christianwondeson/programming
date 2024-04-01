from django.shortcuts import render
from .models import jobPosting

# Create your views here.


def job_list(request):
    job_postings = jobPosting.objects.all()
    return render(
        request, "job_analysis/job_analysis.html", {"job_postings": job_postings}
    )
