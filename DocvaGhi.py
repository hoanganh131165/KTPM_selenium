import  csv
"""with open('taikhoan.csv','w', newline = '') as f:
    fieldName = ['user', 'password']
    writer = csv.DictWriter(f,fieldnames= fieldName)
    writer.writeheader()
    writer.writerow({'user' :'2054050005','password': 'Anh1311mo'})"""

with open('venv/taikhoan.csv', 'r', newline ='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        user = row['user']
        password = row['password']

print(user)
print(password)