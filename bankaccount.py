class BankAccount:
	def __init__(self, account_number = 0, balance = 0):
		self.account_number = account_number
		self.balance = balance
		self.left = None
		self.right = None
	
	def __str__(self):
		return f"Account number: {self.account_number}\n" \
		       f"Balance: {self.balance}"

class BankAccountManager:
    def __init__(self):
        self.root = None

    def add_account(self, account):
        if self.root is None:
            self.root = account
        else:
            self._add_account(self.root, account)

    def _add_account(self, node, account):
        if account.balance < node.balance:
            if node.left is None:
                node.left = account
            else:
                self._add_account(node.left, account)
        else:
            if node.right is None:
                node.right = account
            else:
                self._add_account(node.right, account)

    def deposit(self, account, amount):
        account.balance += amount
        return amount

    def withdraw(self, account, amount):
        if account.balance >= amount:
            account.balance -= amount
            return amount
        else:
            return "Insufficient funds."

    def create_account(self):
        account_number = int(input("Enter account number: "))
        balance = float(input("Enter initial balance: "))
        new_account = BankAccount(account_number, balance)
        self.add_account(new_account)
        print("Account created successfully.")

    @staticmethod
    def display_menu():
        print("=====Menu=====")
        print("1. My account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Create account")
        print("5. Exit")
        print("==============")

    def handle_choice(self, choice):
        if choice == 1:
            user_account_number = int(input("Account Number: "))
            account = self.find_account(self.root, user_account_number)
            if account:
                print(f"Your account: \n{account}")
            else:
                print("Account not found.")
        elif choice == 2:
            user_account_number = int(input("Account Number: "))
            account = self.find_account(self.root, user_account_number)
            if account:
                user_amount = float(input("Amount: "))
                self.deposit(account, user_amount)
                print(f"The balance has been successfully replenished.")
            else:
                print("Account not found.")
        elif choice == 3:
            user_account_number = int(input("Account Number: "))
            account = self.find_account(self.root, user_account_number)
            if account:
                user_amount = float(input("Amount: "))
                self.withdraw(account, user_amount)
                print(f"Money has been successfully withdrawn.")
            else:
                print("Account not found.")
        elif choice == 4:
            self.create_account()
        else:
            exit()

    def find_account(self, node, account_number):
        if node is None:
            return None
        if node.account_number == account_number:
            return node
        elif account_number < node.account_number:
            return self.find_account(node.left, account_number)
        else:
            return self.find_account(node.right, account_number)

account_manager = BankAccountManager()

while True:
    account_manager.display_menu()
    choice = input("Enter your choice: ")
    try:
        choice = int(choice)
        account_manager.handle_choice(choice=choice)
    except ValueError:
        print("Invalid choice. Please enter a number.")
