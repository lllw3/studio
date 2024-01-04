# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 17:36:38 2020

@author: Lenovo
"""


class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day

    def birth_info(self):
        print("The birth is %s-%s-%s"%(self.year,self.mon,self.day))

class People:
    def __init__(self,name,age,year,mon,day):
        self.name=name
        self.age=age
        self.birth=Date(year,mon,day)

    def walk(self):
        print("%s is walking"%self.name)

class Teacher(People):
    def __init__(self,name,age,year,mon,day,course):
        People.__init__(self,name,age,year,mon,day)
        self.course=course

    def teach(self):
        print("%s is teaching"%self.name)

class Student(People):
    def __init__(self,name,age,year,mon,day,group):
        People.__init__(self,name,age,year,mon,day)
        self.group=group

    def study(self):
        print("%s is studying"%self.name)
t1=Teacher("alex",28,1989,9,2,"python")
s1=Student("jack",22,1995,2,8,"group2")
print(t1.name)
t1.walk()
t1.teach()