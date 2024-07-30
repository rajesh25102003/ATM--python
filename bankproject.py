class CheckPin:
    def verify(self,pin):
        if pin==1111 or pin==2222 or pin==3333:
            return True
        else:
            return False

class Balance:
    def __init__(self):
        self.bal=2000
    def getBalance(self):
        return self.bal
    
class Transaction:
    b=Balance()
    def process(self,amt):
        pass
        
class Withdraw(Transaction):
    def process(self,amt):
        if amt<=self.b.bal:
            print("amount withdrawn is ",amt)
            self.b.bal=self.b.bal-amt
            print("Remaining balnce is ",self.b.getBalance())
            print("transaction sucessful..")
        else:
            print("insufficient funds")

class Deposit(Transaction):
    def process(self,amt):
        print("amount deposit is ",amt)
        self.b.bal=self.b.bal+amt
        print("Balance is  ",self.b.getBalance())
    
        
        
        
class ATM:
    count=0
    while True:
        pin=int(input("enter pin number"))
        if pin>=1000 and pin<=9999:
            cpn=CheckPin()
            k=cpn.verify(pin)
            if k:
                print("enter ur choice")
                print("1. withdraw  2.Deposit")
                ch=int(input())
                if ch==1:
                    amt=int(input("Enter an amount for withdrawl"))
                    if amt >0 and amt%100==0:
                        wd=Withdraw()
                        wd.process(amt)
                        break
                    
                    else:
                        print("invalid amount")
                        break
                elif ch==2:
                    amt=int(input("Enter an amount for deposit"))
                    if amt >0 and amt%100==0:
                        de=Deposit()
                        de.process(amt)
                        break
                    else:
                        print("invalid amount")
                        break
                else:
                    print("Invalid choice")
            else:
                print("invalid pin")
                count=count+1
                if count==3:
                    print("blocked")
                    break
        else:
            print("incoorect pin")
            count=count+1
            if count==3:
                print("blocked")
                break
                  
                
                    
                    










                
            
