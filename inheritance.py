#create parent Class
class User():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def show_user(self):
        print('User details :\n')
        print(f'Name :{self.name}\n')
        print(f'Age :{self.age}\n')
        print(f'Sex :{self.sex}\n')

#create child class inheriting the user
class Bank(User):
    def __init__(self,name,age,sex,sold):
        super().__init__(name,age,sex)
        self.sold=sold
    def deposit(self,amount):
        self.amount=amount
        self.sold +=self.amount
        print(f'Your sold has been updated to:{self.sold} DH')
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.sold:
            print(f'Your sold is insufficiant. Sold availabale is :{self.sold}')
        else:
            self.sold -=self.amount
            print(f'You have withdrawed {self.amount}. Your sold is now :{self.sold}')
    def get_sold(self):
        self.show_user()
        print(f'Your Account sold is : {self.sold}')

# Testing the bank system
def main():
    #create a user
    user= User('Hankar Mustapha',32,'Male')
    user.show_user()
    # instanciate a bank acount
    s_account=Bank('Mira Agouzoul',43,'Female',10000)
    print('Make your choice. Do you want to :[1:Deposit,2: Bank Statement,3:Widhdraw]')
    choice=int(input())
    if choice == 1:
        #depost some money
        deposit_amnt=int(input('How much do you want to deposit'))
        s_account.deposit(amnt)
        #show bank statement after deposit
        s_account.get_sold()

    elif choice == 2:
        # get the bank statement
        s_acount.get_sold()
    else:
        withdraw_amnt=int(input('How much money do you want to withdraw ?'))
        #now get some money from my account
        s_account.withdraw(withdraw_amnt)
        # show bank statement after withdraw
        s_acount.get_sold()

#Execution
if __name__=='__main__':
    main()
