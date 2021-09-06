def greetings_function() -> print:
    
    number = int(input('Enter a number: '));
    division = number%2
    if(not division):
        return print('The number is even')
    else :
        return print('The number is odd')

class NewClass:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def printValues(self):
        print('your name: ',self.name, ', your age: ', self.age)

class AnotherClass(NewClass):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, age)
        self.surname = surname
    
    def printValues(self):
        print('your name: ', self.name, ', your surname: ', self.surname, ', your age: ', self.age)

person1 = NewClass('jakub',26)
person2 = AnotherClass('Herald', 'Newman', 99)

person1.printValues()
person2.printValues()



'''
count_file = open('countries.txt', 'a')
count_file.write('\nChina')
count_file.close()
'''
