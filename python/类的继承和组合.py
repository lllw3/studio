# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 17:50:22 2020

@author: Lenovo
"""


##定义一个父类
class father:  ##类的属性 名字 类型名 时间年月日
    def __init__(self,name,typename,year,mon,day):
        self.name=name
        self.typename=typename
        self.timeT=Date(year,mon,day)
    
    def sayMyname(self):
        return self.name+'是我的名字'
    
    def sayHi(self):
        print("跟大家问好")
    
    def saysomething(self):
        print("再一次向大家问好")
        
##定义一个日期类组合时间 实现类的组合
class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    
    def time(self):
        time=str(self.year)+'-'+str(self.mon)+'-'+str(self.day)
        return time
    
    def timeMsg(self):
        timeT=self.time()
        print("The time is "+timeT)
##定义一个父类的子类 实现单继承
class son(father):  ##继承类的属性
    def __init__(self,name,typename,year,mon,day,ID):
        father.__init__(self,name,typename,year,mon,day)
        self.ID=ID
    
    def staticmethodtest():
        return "hello"
    
    def Myname(self):
        print("%s 是子类调用父类的属性"%self.name)
        
    def sonsayhi(self):
        print("子类调用父类的方法:")
        return self.sayHi()
    
    def saysomething(self):
        print("%s 再一次向大家问好,这是子类对父类的重构方法"%self.name)
##定义一个父类的孙子类 实现多重继承
class grandson(son,father):
    def __init__(self,name,typename,year,mon,day,ID):
        father.__init__(self,name,typename,year,mon,day)
        son.__init__(self,name,typename,year,mon,day,ID)
            
    def test(self):
       print(father.sayMyname(self))
       return son.Myname(self)
    
if __name__=='__main__':
    ##实例化子类
    ME=son("www",'classson',2001,9,7,"teenager")
    KK=grandson("www",'classson',2001,9,7,"teenager")
    ##输出
    print(ME.name+' '+ME.typename+' '+ME.timeT.time()+" "+ME.ID)
    ##调用测试
    ME.timeT.timeMsg()
    ME.Myname()
    ME.sonsayhi()
    ME.saysomething()
    KK.test()
    