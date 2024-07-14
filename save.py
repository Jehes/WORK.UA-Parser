import csv
import time
language_choice = int(
    input("Choose the infolist language: \n1 - English \n2 - Ukrainian\n"))
if language_choice == 1:
    job_infolist = ['Job Name', 'Company/Organization', 'Location', 'Link']
elif language_choice == 2:
    job_infolist = ['Назва вакансії', 'Компанія/Організація',
                    'Місцезнаходження', 'Посилання']
else:
    print("Invalid value! Restart the program")
    time.sleep(3)
    exit()


def save_to_csv(jobs):
    file = open('parsed.csv', mode='w', encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(job_infolist)
    for job in jobs:
        writer.writerow(list(job.values()))
