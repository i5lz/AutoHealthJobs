# reports/excel_report.py
import pandas as pd
from datetime import datetime

def generate_excel(jobs):
    df = pd.DataFrame(jobs)
    filename = f"job_report_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    df.to_excel(filename, index=False)
    return filename
