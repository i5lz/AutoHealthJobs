# scrapers/moh_scraper.py
import requests
from bs4 import BeautifulSoup

def get_moh_jobs():
    url = "https://www.moh.gov.sa/en/Ministry/Employment/Pages/default.aspx"
    jobs = []

    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select("a[href*='health'], a[href*='تثقيف']")

        for a in links:
            jobs.append({
                "title": a.get_text(strip=True),
                "company": "وزارة الصحة",
                "location": "المملكة العربية السعودية",
                "link": a["href"] if a["href"].startswith("http") else f"https://www.moh.gov.sa{a['href']}",
                "source": "MOH"
            })
    except Exception as e:
        print(f"MOH jobs failed: {e}")
    return jobs
