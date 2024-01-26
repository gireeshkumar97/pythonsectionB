class aswiniError(Exception):
    pass
class MobilenameError(Exception):
    pass
name=input('enter a name:-')

if len(name)<=4:
    raise aswiniError(f'name should be more than 4 character but {len(name)}were given')
else:
    print('name is validated')

mob=input('enter a name')
if len (name)<4:
    MobilenameError(f'name should be more than than 4 characters{len(name)}were given')
else:
    print('name is validated')