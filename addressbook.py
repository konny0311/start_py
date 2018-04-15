class AddressBook:
    person_list = []

    def add(self, person):
        self.person_list.append(person)
    def show_all(self):
        for person in self.person_list:
            print(person.lastname + ' ' + person.firstname)
    def search(self, keyword):
        for person in self.person_list:
            if keyword in person.lastname or keyword in person.firstname:
                print(person.lastname + ' ' + person.firstname)

    def import_data(self, file):
        import csv
        import datetime

        with open(file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)

            for row in reader:
                p = Person()
                p.lastname = row[0]
                p.firstname = row[1]
                p.email = row[2]
                p.birthday = datetime.datetime.strptime(row[3], "%Y/%m/%d")
                p.tel = row[4]

                self.person_list.append(p)

class Person:
    import datetime

    firstname = ''
    lastname = ''
    tel = ''
    email = ''
    birthday = datetime.datetime(1991, 3, 11)

ab = AddressBook()

ab.import_data('sample100.csv')
print('一覧表示')
ab.show_all()
print('沢井さんの判定')
ab.search('沢井')
