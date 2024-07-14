import requests
from bs4 import BeautifulSoup
import time

URL = input("Enter WORK.UA link: ")
if not URL.startswith("https://www.work.ua/"):
        print("Link is not valid! Restart the program")
        time.sleep(3)
        exit()
def find_max_page():
    request = requests.get(URL)
    soup = BeautifulSoup(request.text, 'html.parser')
    pages = []
    paginator = soup.find_all(
        "a", {'class': 'ga-pagination-default pointer-none-in-all'})
    for page in paginator:
        pages.append(int(page.text))
    return pages[-1]


def find_job(html):
    title = html.find("a").text
    link = html.find("a")['href']
    link = URL.rsplit('/',1)[0] + link
    company = html.find(
        'div', {'class': 'mt-xs'}).find('span', {'class': 'strong-600'}).get_text()
    company_check = html.find(
        'div', {'class': 'mt-xs'}).find('span', {'class': ''}).find('span', {'class': 'strong-600'})
    one_location_element = html.find('div', {'class': 'mt-xs'}).find('span')
    location_element = html.find('div', {'class': 'mt-xs'}).find_all('span', {'class': ''})
    if len(location_element) >= 2:
            location = location_element[1].get_text()
            location = location.partition(',')[-1]
            if company_check == None:
                location = location_element[-1].get_text()
                location = location.partition(',')[-1]
                if location_element[1] != one_location_element:
                    location = location_element[0].get_text() 
                    location = location.partition(',')[0]
    else:
            location = location_element[0].get_text() 
            location = location.partition(',')[0]
    location = location.strip()
    location = location.replace(',', '')
    return {"job_name": title,"company":company,"location": location, "link":link}


def find_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print("Data page processing: ", page)
        result = requests.get(f'{URL}?page={page}')
        result_soup = BeautifulSoup(result.text, 'html.parser')
        results = result_soup.find_all('div', {
            'class': 'job-link'})
        for result in results:
                job = find_job(result)
                jobs.append(job)
    return jobs
def get_jobs():
        max_page = find_max_page()
        jobs = find_jobs(max_page)
        return jobs
         