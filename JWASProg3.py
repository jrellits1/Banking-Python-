# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:37:03 2019

@author: Josh Stiller
"""
#Josh Stiller 
#This is my first class which is JWASAccount this is where a lot of reference is made and is overall a very important class
class JWASAccount(object): 

    
    def __init__(self,balance,accountstatus): #this is where we get our account balance and status. 
        self.accountstatus = accountstatus
        self.balance = balance
      #this is the beginning of the deposit function        
    def deposit(self,num=0):
        if self.accountstatus == 1:
                self.balance = self.balance + num
                print ('New Balance after $', num, 'deposit is $', self.balance)
     #and the get owner function where we are printing out the name of the client (which is stored in the main) and the word "owner" so 
     # the owner is easier to identify.            
    def getOwner(self):
        print ('Owner:',self.name)
    # the same goes foor acocunt number. It is simply grabbing information. 
    def getAccountNumber(self):
        print ('Account Number:',self.accountnumber)
    #this is how we close the current account funtion. 
    def close(self):
        self.accountstatus = 0
        print('Account Successfully Closed')

#this is the checking account where the is the assigning of a random account number(notice this is referencing JWASAccount)
class JWASChecking(JWASAccount):
    def __init__(self, name, accountnumber, balance=0, transactionfee=0):
        super().__init__(balance,1)
        self.name = name
        self.balance = balance
        "self.accountnumber = random.randint(123456789,999999999)"
        self.accountnumber = accountnumber
        self.transactionfee = transactionfee
        print('Checking Account: ')
      #and here is the withdraw function that withdraws the set balance and then returns the balance as a print statement
    def withdraw(self,num=0):
        if num < self.balance:
                if self.accountstatus == 1:
                    self.balancenew = self.balance - self.transactionfee
                    print ('$', self.balancenew, 'is your new balance becuase of', '$', self.transactionfee, 'transaction fee amount')
        else:
            print('not enough funds')  
 #if there is less money in the account than the withdrawl amount it will throw an error. 
    

#this class focuses on the individual person and gets all the needed information
class JWASPerson(JWASAccount):
    def __init__(self, name, accountnumber, age=0):
        super().__init__(age,1)
        self.name = name
        self.accountnumber = accountnumber
        self.age = age
        print('Personal Account Information: ')
        
#this is the business account which also references JWASAccount and has withdrawl.     
class JWASBusiness(JWASAccount):
    def __init__(self, name, accountnumber, balance=0):
        super().__init__(balance,1)
        self.name = name
        self.balance = balance
        "self.accountnumber = random.randint(123456789,999999999)"
        self.accountnumber = accountnumber
        print('Business Account:')
        
    def withdraw(self,num=0):
        if num < self.balance:
                if self.accountstatus == 1:
                    self.balance = self.balance - num
                    print ('$ Withdrawal Amount =', num, ':', '$', self.balance, 'is your new balance')
        else:
            print('not enough funds')
#the saving is basically the same as all the rest. Lets be real they are all the same with different names.
class JWASSavings(JWASAccount):
    def __init__(self, name, accountnumber, balance=0, wfee=0):
        super().__init__(balance,1)
        self.name = name
        self.balance = balance
        "self.accountnumber = random.randint(123456789,999999999)"
        self.accountnumber = accountnumber
        self.wfee = wfee
      
        
    def withdraw(self,num=0):
        if num < self.balance:
                if self.accountstatus == 1:
                    self.balance = self.balance - num
                    print ('$ Withdrawal Amount =', '$', num, ':', '$', self.balance, 'is your new balance')
        else:
            print('not enough funds')

  #this one is, again, like the others only it has an age requirement of 21.   
class JWASTrust(JWASSavings):
    def __init__(self, name, accountnumber, balance=0, interestRate=0, age=0):
        super().__init__(balance,1)
        self.name = name
        self.balance = balance
        "self.accountnumber = random.randint(123456789,999999999)"
        self.accountnumber = accountnumber
        self.interestRate = interestRate
        self.age = age
        print('Trust Account:')
        
    def withdraw(self,num=0):
        if num < self.balance:
                if self.accountstatus == 1:
                    if self.age >= 21: #see here is the age thing. 
                        self.balance = self.balance - num
                        print ('$', self.balance, 'is your new balance')
                    else:
                        print('FAILED: Too young to withdraw')
        else:
            print('not enough funds')
    #this is the main. It has all the information that is called throughout program. 
def main():
    checking = JWASChecking('Joshua Stiller', 2589985, 550,3)
    checking.deposit(100)
    checking.withdraw(100)
    checking.getOwner()
    checking.getAccountNumber()
    checking.close()
    checking.withdraw(100)
    print('\n')
    personal = JWASPerson('Joshua Stiller', 2589985)
    personal.getOwner()
    personal.getAccountNumber()
    personal.close()
    print('\n')
    business = JWASBusiness('IBM', 2589985, 5000)
    business.deposit(500)
    business.withdraw(100)
    business.getOwner()
    business.getAccountNumber()
    business.close()
    print('\n')
    print('Savings Account:')
    savings = JWASSavings('Joshua Stiller', 2589985, 5000, 2.75)
    savings.deposit(250)
    savings.withdraw(50)
    savings.getOwner()
    savings.getAccountNumber()
    savings.close()
    savings.withdraw(50)
    print('\n')
    trust1 = JWASTrust('Joshua Stiller: Can withdrawal when 21', 2589985, 5000, 10.95, 18)
    trust1.deposit(350)
    trust1.withdraw(250)
    trust1.getOwner()
    trust1.getAccountNumber()
    trust1.close()
    trust1.withdraw(200)
    
    #main main main .
"Run the main function"   
if __name__== "__main__":
  main() 
