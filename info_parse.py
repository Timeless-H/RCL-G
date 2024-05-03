import requests
from bs4 import BeautifulSoup

def get_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the web page content.")
        return None
    
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

# .find("p").get_text()
# .find_all("p")
# Extract job details
# job_title = soup.find('h1').text.strip()  # Assuming the job title is in an <h1> tag
# job_description = soup.find('div', class_='job-description').text.strip()  # Assuming job description is in a <div> with class 'job-description'
# company_vision = soup.find('div', id='company-vision').text.strip()  # Assuming company vision is in a <div> with id 'company-vision'
# company_mission = soup.find('div', id='company-mission').text.strip()  # Assuming company mission is in a <div> with id 'company-mission'

get_info("https://ca.indeed.com/cmp/Earthdaily-Agro/jobs?jk=b963d95ad02c01cd&start=0&clearPrefilter=1")  