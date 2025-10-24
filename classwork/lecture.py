import csv
data = [{
         "Name": "Alice",
         "Age": "28",
         "City": "New York"}, 
         {
          "Name":"Johan",
          "Age": "18",
          "City": "Fairfax"
         }]

with open("people.csv", "w", newline= "") as file:
    fieldnames = ["Name", "Age", "City"]
    #takes in 2 parameters with the fieldnames equaling the variable we named fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open("people.csv", "r" ) as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row["Name"]} is {row["Age"]} and lives in {row["City"]}")