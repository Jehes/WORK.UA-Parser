from work import get_jobs as get_workua_jobs
from save import save_to_csv

save_to_csv(get_workua_jobs())

print("Done! Check the parsed.csv file in the current folder


")