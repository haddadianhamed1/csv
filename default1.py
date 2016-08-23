from collections import defaultdict
import csv
from pprint import pprint

d = defaultdict(list)
with open('test2.csv', 'rb') as f:
    reader = csv.DictReader(f, delimiter=',')   
    for row in reader:
        d[(row["Vulnerability Title"], row["Vulnerability Severity Level"])].append(row["Asset IP Address"])   

pprint(d)
with open('final.csv' , 'wb') as csv_file:	
	writer = csv.writer(csv_file)
	writer.writerow(["Vulnerability Title" , "Asset IP Address"])
	for key, value in d.items():
		writer.writerow([key, value])

