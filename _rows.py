rows=int(input('enter the number of rows'))
temp=rows//2
out=''
for i in range (rows):
    for j in range (rows):
        if i==temp or i== temp:
            out+='   '
        else:
            out+='* '
    out+='\n'
name =input('Enter the file name')
with open(f'{name}.txtq','w') as file:
    file.write(out)
    