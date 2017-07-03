#!/usr/bin/env python
# coding=utf-8
class BaseClass:    
    def __init__(self):
        self.name = 'BaseClass'
        print('BaseCalss: Constructor called')
    def getname(self):
        print('BaseCalss: self name equals ' + self.name)
 
class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print('DerivedClass: Constructor called')
    def getname(self):
        print('self.name init value is ' + self.name)
        self.name = 'DerivedClass'
        print('DerivedClass: self name equals ' + self.name)
 
if __name__ == '__main__':
    class1 = BaseClass()
    class1.getname()
    
    class2 = DerivedClass()
    class2.getname()
