import requests

def get_number_of_jobs_T(api_url, technology):
    """Return the number of jobs requiring a given technology."""
    r = requests.get(api_url)
    data = r.json()
    jobs=[]
    for job in data:
        tech = job.get("Key Skills")
        if technology in tech:
            jobs.append(job)
    number_of_jobs = len(jobs)
    return technology,number_of_jobs

def get_number_of_jobs_L(api_url, location):
    """Return the number of jobs located in a certain location."""
    r = requests.get(api_url)
    data = r.json()
    jobs=[]
    for job in data:
        loc = job.get("Location")
        if loc in location:
            jobs.append(job)
    number_of_jobs = len(jobs)
    return location,number_of_jobs