import csv
#file=open('sample.csv', 'w')
with open ('sample.csv','w')as file:
    data=[
        [1,'Gireeh kumar reddy',21],
        [2,'Mohammad Bilal',22],
        [3,'MOhammad kashif'],23,
        [4,'Prashanthii',24],

         ]
    record=csv.writer(file)
    record.writerows(data)