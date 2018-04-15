class A:
    def hello(self):
        print('class A says hello')
class B(A):
    def hello(self):
        print('class B says hello')

b = B()
b.hello()
