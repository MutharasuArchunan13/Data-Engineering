import csv
import time
from collections import defaultdict

start = time.time()

high_salary_jobs = []
job_salary_sum = defaultdict(list)
company_job_count = defaultdict(int)

with open("job_descriptions.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            salary_range = row["Salary Range"]
            if "$" in salary_range and "K" in salary_range:
                low = int(salary_range.strip().split("-")[0].replace("$", "").replace("K", "")) * 1000
                if low > 1000:
                    job_title = int(row["Job Title"])
                    company = row["Company"]
                    location = row["location"]

                    high_salary_jobs.append((job_title, low, location, company))
                    job_salary_sum[job_title].append(low)
                    company_job_count[company] += 1
        except Exception:
            continue

print(f"Total high salary jobs: {len(high_salary_jobs)}")

print("\nTop 10 Companies by Job Count:")
top_companies = sorted(company_job_count.items(), key=lambda x: x[1], reverse=True)[:10]
for company, count in top_companies:
    print(f"{company}: {count} jobs")

print("\nTop 10 High Paying Job Titles:")
avg_salary_by_title = [(k, sum(v) // len(v)) for k, v in job_salary_sum.items()]
top_titles = sorted(avg_salary_by_title, key=lambda x: x[1], reverse=True)[:10]
for title, avg in top_titles:
    print(f"{title}: {avg}")

print(f"\nTime taken (Python): {time.time() - start:.2f} seconds")
