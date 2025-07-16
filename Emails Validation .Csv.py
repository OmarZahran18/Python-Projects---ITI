import csv  

domains = set()

with open("D:\\Emails.csv", "r", newline="", encoding="utf-8") as file:  
    reader = csv.reader(file)

    next(reader) 

    for row in reader:
        email = row[3].strip()
        
        if "@" in email and email.count("@") == 1 and " " not in email:
            name, domain = email.split("@")
            if "." in domain:
                domains.add(domain)  

for d in domains:
    print(d)
