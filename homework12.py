import csv

#Exercise N1

with open('titanic.csv', 'r') as file:
    csv_dict_reader = csv.DictReader(file)
    survived = []
    for row in csv_dict_reader:
        if row['Survived'] == '1':
            survived.append(row)
        else:
            pass
with open('survived.csv', 'w', newline='') as file:
    fieldnames = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(survived)


#Exercise N2

with open('organizations-100.csv', 'r') as file:
    csv_dict_reader = csv.DictReader(file)
    sorted_lst = list(csv_dict_reader)

sorted_lst.sort(key=lambda row: int(row['Number of employees']))

with open('sorted_csv.csv', 'w', newline='') as file:
    fieldnames = ['Index','Organization Id','Name','Website','Country','Description','Founded','Industry','Number of employees']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(sorted_lst)

#Exercise N3

secure_companies = []
with open('organizations-100.csv', 'r') as file:
    csv_dict_reader = csv.DictReader(file)
    for row in csv_dict_reader:
        info = {'Organization Id': row['Organization Id'], 'Name': row['Name'], 'Website': row['Website'], 'Industry': row['Industry'], 'Number of employees': row['Number of employees']}
        if row['Website'][0:5]=='https':
            secure_companies.append(info)
with open('ssl_companies.csv', 'w', newline='') as file:
    fieldnames = ['Organization Id','Name','Website','Industry','Number of employees']
    csv_dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(secure_companies)