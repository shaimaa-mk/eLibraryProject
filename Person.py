#main charecters for e-library sysy

#parent class person
import time
import datetime
class Person:

    def __init__(self, name, age):
        self._id = str(round(time.time()*1001))
        self._name = name
        self._age = age

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age


    #modify propreties
    def setId(self, id):
        self._id = id

    def setName(self, name):
        self._name = name

    def setAge(self,age):
        self._age

    def get_Person(self):
       pass


#children classes

class Client(Person):

    def __init__(self, name, age, phone):
        self._phone = phone
        super().__init__(name, age )
        print("A client has created with ID %s" % self.getId())
        #print('A client called %s has created and your ID is %s'%name%self.getId())

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def get_Person(self):
        return {
            "ID": self._id,
            "Name": self._name,
            "Age": self._age,
            "Phone": self._phone
        }


class Librarian(Person):

    def __init__(self, name, age, type ):
        self._emplyType = type
        super().__init__(name, age)
        print("An emplyee called" )
        #print("An emplyee called %s has created and your ID is %s"% name ,self.getId())

    def getType(self):
        return self._emplyType

    def setType(self, type):
        self._emplyType = type

    def get_Person(self):
        return {
            "ID": self._id,
            "Name": self._name,
            "Age": self._age,
            "Phone": self._emplyType
        }
