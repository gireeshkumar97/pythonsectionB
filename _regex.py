import re
# data =re.findall('[0-9]','abcdef12gh45')
# print(data)
with open (r"C:\Users\Administrator.MCA\Desktop\mtca.txt",'r+')as file:
    data =file.read()
    newdata=re.sub(' ','_',data)
    file.seek(0)
    file.write(newdata)
 