# scrapers/google_jobs_scraper.py
import requests

def get_google_jobs():
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_jobs",
        "q": "أخصائي تثقيف صحي OR Health Educator OR Public Health",
        "hl": "en",
        "location": "Saudi Arabia",
        "api_key": "YOUR_SERPAPI_KEY"
    }

    jobs = []
    try:
        res = requests.get(url, params=params)
        results = res.json().get("jobs_results", [])

        for job in results:
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "link": job.get("related_links", [{}])[0].get("link", "#"),
                "source": "Google Jobs"
            })
    except Exception as e:
        print(f"Google Jobs failed: {e}")
    return jobs
