#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import sys

# Define the job keywords you want to search for
job_keywords = ["Data Scientist"]
df=pd.read_csv(sys.argv[1],header=None, index_col=0)

# Define the list of career page URLs to scrape
career_urls=dict(zip(df[1].keys(),df[1].values))

# Helper function to search for jobs on a single website
def check_job_openings(url, job_keywords):
    try:
        # Send a request to the website
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text that may contain job titles
        page_text = soup.get_text().lower()

        # Search for job keywords in the page text
        for keyword in job_keywords:
            if re.search(keyword.lower(), page_text):
                return f"Found '{keyword}' position at {url}"
        
        # If no job title found
        return f"No positions found at {url}"
    
    except requests.exceptions.RequestException as e:
        return f"Failed to access {url}: {e}"

# Iterate over each company and check for job openings
results = []
for company, url in career_urls.items():
    result = check_job_openings(url, job_keywords)
    print(f"{company}: {result}")
    results.append({"Company": company, "Result": result})
    
    # Add delay to avoid being blocked
    time.sleep(2)

# Optional: save the results to a CSV file for record-keeping
df = pd.DataFrame(results)
df.to_csv("job_openings_results.csv", index=False)

