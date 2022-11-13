#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Challenge 1 SquareSum
class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x**2
        b = self.y**2
        c = self.z**2
        sum = a+b+c
        return sum
square = Point(1,3,5)
square.sqSum()


# In[3]:


# Challenge 2 Calculation
class Calculator:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        a = self.num1 + self.num2
        return a
    def subtract(self):
        s = self.num2 - self.num1
        return s
    def multiply(self):
        m = self.num1 * self.num2
        return m
    def divide(self):
        d = self.num2/self.num1
        return d
calculation = Calculator(10,94)
print(calculation.add())
print(calculation.subtract())
print(calculation.multiply())
print(calculation.divide())


# In[4]:


# Challenge 3 Student Details
class Student:
    __Name = "PRASAD"
    __RollNumber = 29  
    def getName(self):
        print("getName called")
        print( Student.__Name)
    def setName(self,N):
        print("setName called")
        Student.__Name = N
        print(Student.__Name)
    def getRollNumber(self):
        print("getRollNumber called")
        print( Student.__RollNumber)
    def setRollNumber(self,R):
        print("setRollNumber called")
        Student.__RollNumber = R
        print(Student.__RollNumber)
a = Student()
a.getName()
a.setName("Sunny")
a.getRollNumber()
a.setRollNumber(69)


# In[5]:


# Challenge 4 Bank Account
class Account:
    def __init__(self,title = None,balance = 0):
        self.title = title
        self.balance = balance
        print("MR",str(self.title) + " your balance is : " +str(self.balance))
class SavingsAccount(Account):
    def __init__(self,title,balance,intrest):
        super().__init__(title,balance)
        self.intrest = intrest
        print("MR",str(self.title) + "  your balance is :  " +str(self.balance)+" and your intrest is :  "+str(self.intrest))
Bank1 = SavingsAccount("Prasad",1000,5)


# In[10]:


# Challenge 5 Handling Bank Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        #print("After withdraw your remaining balance is :",self.balance)
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        #print("After deposit your remaining balance is :",self.balance)
        return self.balance
        
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        self.interestamount = (self.interestRate*self.balance)/100 
        return int(self.interestamount)
class Savingsclass(SavingsAccount):
    def __init__(self,title,balance,intrestRate):
        super().__init__(title,balance,intrestRate)

Bank = Savingsclass("Prasad",2000,5)
print(Bank.deposit(500))
print(Bank.withdraw(500))
print(Bank.getBalance())
print(Bank.interestAmount())


# In[11]:


# Challenge Normally Handling Bank Account
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        #print("After withdraw your remaining balance is :",self.balance)
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        #print("After deposit your remaining balance is :",self.balance)
        return self.balance
        
    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        self.interestamount = (self.interestRate*self.balance)/100 
        return int(self.interestamount)

Bank = SavingsAccount("Prasad",2000,5)
print(Bank.deposit(500))
print(Bank.withdraw(500))
print(Bank.getBalance())
print(Bank.interestAmount())


# In[ ]:




