# Job\_Search README
Author: McKay Osborne, 11/17/2024

`## Project Title:
Job\_Search

## Project Description:
This is a Python package is used for finding jobs on user-specified career pages that match a given search criteria and checks for potential matches from what the employer is looking for and the skillset of the applicant.

## Required packages:
- Python
- BeautifulSoup
- requests
- re
- Pandas

## How to Run
``` $:/  run_search.py <path to job site dictionary text file> ```

## How it works
1. A dictionary is created using the comma delimited file where the keys are company name and the value is the url to the career page.
2. Using this dictionary, the code tries to search for the job title(s) on the page.
3. For each company, there is message that is printed out whether or not there are jobs to apply for.


## Dictionary text file Example
### Example.txt

```
Company 1, company1\_url
Company 2, company2\_url
:
:
:
```





