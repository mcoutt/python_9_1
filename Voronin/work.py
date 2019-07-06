import csv

with open('stud.csv', 'w', newline='') as f:
    headers = ['fname', 'lname', 'phone', 'gender', 'email']
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()    
    for i in range(30):
        writer.writerow({
            'fname': f'Nickname{i}',
            'lname': f'Fon{i}',
            'phone': f'0981234567{i}',
            'gender': f'm{i}',
            'email': f'some_mail{i}@ex.com'
            })
