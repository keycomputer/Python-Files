import csv 
header = ["Firstname","Lastname"]

with open("names.csv" ,"w", newline="") as csvfile:
    writer  = csv.DictWriter(csvfile , fieldnames=header)
    writer.writeheader()
    writer.writerow({"Firstname": "a10", "Lastname": "a20"})
    writer.writerow({"Firstname": "a11", "Lastname": "a21"})
    writer.writerow({"Firstname": "a12", "Lastname": "a22"})
    writer.writerow({"Firstname": "a13", "Lastname": "a23"})
