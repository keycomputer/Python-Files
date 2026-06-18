import csv 
header = ["Firstname","Lastname"]
data = [{"Firstname": "a10", "Lastname": "a20"},
        {"Firstname": "a11", "Lastname": "a21"},
       {"Firstname": "a12", "Lastname": "a22"},
       {"Firstname": "a13", "Lastname": "a23"}]
with open("name2.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header )
    writer.writeheader()
    for i in data:
        writer.writerow({"Firstname" : i['Firstname'], "Lastname": i['Lastname']})
