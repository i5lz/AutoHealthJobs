# filters/keyword_filter.py
KEYWORDS = [
    "تثقيف صحي", "تعزيز الصحة", "أخصائي", "مثقف صحي",
    "Health Educator", "Health Promotion", "Public Health", "Community Health"
]

def filter_jobs(jobs):
    filtered = []
    for job in jobs:
        text = job["title"].lower()
        if any(keyword.lower() in text for keyword in KEYWORDS):
            filtered.append(job)
    return filtered
