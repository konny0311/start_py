class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0
    weight = 0.0

a = Human()
a.age = 27
a.lastname = 'Last'
a.firstname = 'First'
a.height = 170
a.weight = 56

print(str(a.age) + '歳の' + a.firstname + ' ' + a.lastname + 'です。')
