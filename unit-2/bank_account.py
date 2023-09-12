class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ${amount}. New balance is ${self.__account_balance}."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance is ${self.__account_balance}."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name} ({self.__account_number}): ${self.__account_balance}"
    

if __name__== "__main__":
    
    account1 = BankAccount("123456789", "John Doe", 1000)
    print(account1.display_balance())  
    print(account1.deposit(500))     
    print(account1.withdraw(200))    
    print(account1.withdraw(2000))   
    print(account1.deposit(-100))    
