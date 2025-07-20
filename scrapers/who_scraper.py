# scrapers/who_scraper.py
import requests
from bs4 import BeautifulSoup

def get_who_jobs():
    url = "https://careers.who.int/careersection/ex/jobsearch.ftl"
    headers = {"User-Agent": "Mozilla/5.0"}
    jobs = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.select("tr")

        for row in listings:
            cells = row.find_all("td")
            if len(cells) < 3: continue

            title = cells[0].get_text(strip=True)
            location = cells[1].get_text(strip=True)
            link = "https://careers.who.int" + row.select_one("a")["href"]

            if "health" in title.lower():
                jobs.append({
                    "title": title,
                    "company": "WHO",
                    "location": location,
                    "link": link,
                    "source": "WHO"
                })
    except Exception as e:
        print(f"WHO jobs failed: {e}")
    return jobs
