import fileinput
import csv
import json
url =[]
url2=[]
csvFilePath = "progress.csv"
jsonFilePath = "progress.json"
fac_name ="Harshit Kumar" #facilitator name
id = 0

with open(csvFilePath) as f:
    reader = csv.DictReader(f)
    rows = list(reader)
# Write data to a JSON file ...
with open(jsonFilePath, "w") as f:
    json.dump(rows, f, indent=4)
f = open('progress.json',)# returns JSON object as

data = json.load(f)
for element in data:
    if element['Enrolment Status'] == 'All Good':
        url.append(element['Qwiklabs Profile URL'])
with open('finaluserurl.txt', 'w') as f:
    print(url, file=f)


"""
with fileinput.input(files=('userurl.txt')) as f:
    for line in f:
        url.append(line.replace("\n", ""))
for ele in url:
    if ele.strip():
        url2.append(ele)
print(url2)
with open('finaluserurl.txt', 'w') as f:
    print(url2, file=f)
"""
