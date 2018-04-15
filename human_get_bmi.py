class Human:
    age = 0
    lastname = ''
    firstname = ''
    height = 0.0
    weight = 0.0

    def get_bmi(self):
        return self.weight / ((self.height) ** 2)

a = Human()
a.age = 27
a.lastname = 'Last'
a.firstname = 'First'
a.height = 1.7
a.weight = 56
bmi = a.get_bmi()

print(str(a.age) + '歳の' + a.firstname + ' ' + a.lastname + 'です。')
print('bmiは' + str(bmi) + 'です。')
