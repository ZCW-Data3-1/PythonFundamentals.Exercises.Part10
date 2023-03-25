import pickle


class PersistenceUtils:

    @staticmethod
    def write_pickle():
        b1 = Bank()
        b1.save_data(b1.get_accounts_list())

    @staticmethod
    def load_pickle():
        b1 = Bank()
        accounts = b1.load_data()
        print(accounts)


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

    def get_accounts_list(self):
        cust1 = self.add_customer(123, "brijesh", "s")
        cust2 = self.add_customer(456, "dhannya", "g")
        customer1_account = self.add_account(345, 'savings', cust1, 10000)
        customer2_account = self.add_account(789, 'savings', cust2, 10000)
        accounts = [customer1_account, customer2_account]
        return accounts

    def save_data(self, accounts):
        with open('bank_account.pkl', 'wb') as f:
            pickle.dump(accounts, f)

    def load_data(self):
        with open('bank_account.pkl', 'rb') as f:
            accounts = pickle.load(f)
            return accounts


PersistenceUtils.write_pickle()
PersistenceUtils.load_pickle()
