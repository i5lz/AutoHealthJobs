# scrapers/indeed_scraper.py
import requests
from bs4 import BeautifulSoup

def get_indeed_jobs():
    query = "أخصائي تثقيف صحي OR Health Educator OR Public Health"
    url = f"https://www.indeed.com/jobs?q={query}&fromage=1"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_cards = soup.select(".result")
    jobs = []

    for job in job_cards:
        title = job.select_one("h2.jobTitle span")
        company = job.select_one(".companyName")
        location = job.select_one(".companyLocation")
        link = job.select_one("a")["href"]

        if title and link:
            jobs.append({
                "title": title.get_text(strip=True),
                "company": company.get_text(strip=True) if company else "N/A",
                "location": location.get_text(strip=True) if location else "N/A",
                "link": f"https://www.indeed.com{link}",
                "source": "Indeed"
            })
    
    return jobs
