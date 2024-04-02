from bs4 import BeautifulSoup
import requests
from job_analysis.models import jobPosting
import datetime

def scrape_jobs():
    url = 'https://www.ethiopianreporterjobs.com/jobs-in-ethiopia/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        job_elements = soup.find_all('div', class_= 'job-posting')
        for job_element in job_elements:
            title = job_element.find('h2').text.strip()
            company = job_element.find('p', class_='company').text.strip()
            location = job_element.find('p', class_='location').text.strip()
            skills = job_element.find('ul', class_='skills').text.strip()
            salary = job_element.find('p', class_='salary').text.strip()
            job = jobPosting(
                title = title,
                company = company,
                location = location,
                skills = skills,
                salary = salary,
                posting_date = datetime.datetime.now()
            )
            job.save()
        print("Job postings scraped successfully!")
    else:
        print(f"Failed to scrape job postings. status code: {response.status_code}")