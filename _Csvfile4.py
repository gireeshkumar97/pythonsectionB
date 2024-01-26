import csv 
# #file=open('sample.csv',a')
# with open('new.csv','w',newline='')as csvfile:
#     fieldnames=['id','name','age']
#     record=csv.DictWriter(csvfile,fieldnames)
#     record.writeheader()
#     data=[
#         {'id':1,'name':'Bilal','age':16},
#         {'id':2,'name':'Gireesh','age':12},
#         {'id':3,'name':'Kashif','age':20},
#         {'id':4,'name':'Jessika','age':22}
#     ]
#     record.writerows(data)
with open('new.csv','r',newline='')as file:
    records=csv.DictReader(file)
    for i in records:
        print(i)