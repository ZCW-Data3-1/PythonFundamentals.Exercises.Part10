class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "{} {} {}".format(self.id, self.first_name, self.last_name)


class Account:
    def __init__(self, number, acct_type, owner, balance):
        self.number = number
        self.acct_type = acct_type
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "{} {} {}".format(self.number, self.acct_type, self.owner, self.balance)

    def add_balance(self, money):
        self.balance = self.balance + money

    def minus_balance(self, money):
        self.balance = self.balance - money

    def get_balance(self):
        return self.balance

    def update_balance(self, new_balance):
        self.balance == new_balance


class Bank:
    def add_customer(self, cust_id, first_name, last_name):
        customer = Person(cust_id, first_name, last_name)
        return customer

    def add_account(self, acct_number, acct_type, owner, balance):
        account = Account(acct_number, acct_type, owner, balance)
        return account

    def remove_account(self, number, acct_type, owner, balance):
        pass

    def deposit_money(self, acct_number, deposit_amount, account):
        # search account based on acct_number
        account.add_balance(deposit_amount)

    def withdraw_money(self, acct_number, withdraw_amount, account):
        # search account based on acct_number
        account.minus_balance(withdraw_amount)

    def balance_inquiry(self, acct_number, account):
        print('Balance: ', account.get_balance())


b1 = Bank()
customer1 = b1.add_customer(123, "brijesh", "s")
# print(b2)
customer1_account = b1.add_account(345, 'savings', customer1, 10000)
print(customer1_account)
b1.deposit_money(345, 10000, customer1_account)
b1.withdraw_money(345, 1000, customer1_account)
b1.balance_inquiry(345, customer1_account)

# p11 = Person(1232, "Alice", "Bob")
# print(p11)

# acc1 = Account(123, "savings", "dhamya", 1000000)
# print(acc1)
