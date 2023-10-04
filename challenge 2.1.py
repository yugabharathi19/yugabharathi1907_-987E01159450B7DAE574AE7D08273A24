class bankaccount():
	def __init__(self,account_name="bank account",balance=2400):
	    self.account_name=account_name
	    self.balance=balance
	def deposit(self,value):
		self.balance=self.balance+value
		print("you now have:",self.balance)
	def withdraw(self,value):
		self.balance=self.balance-value
		print("you now have:",self.balance)
class currentaccount(bankaccount):
	def __init__(self,account_name="current account",balance=2400):
	    self.account_name=account_name
	    self.balance=balance
	    super().__init__()
	def withdraw(self,value):
		if value>1000:
		 print("you will have to phone the bank manager")
		else:
		 self.balance=self.balance-value
		 print("you now have:",self.balance)
class savingsaccount(bankaccount):
	def __init__(self,account_name="savings account",balance=2400):
	 self.account_name=account_name
	 self.balance=balance
	 super().__init__()
	def deposit(self,value):
		self.balance=self.balance+(value*1.03)
		print("you now have:",self.balance)
currentobject=currentaccount()
savingsobject=savingsaccount()
while True:
	print("1.current account")
	print("2.saving account")
	menu_option=int(input())
	
	if menu_option==1:
		print("1.deposit funds")
		print("2.withdraw funds")
		submenu_option=int(input())
		if submenu_option==1:
			value=int(input("how much would you like to deposit"))
			currentobject.deposit(value)
		elif submenu_option==2:
			value=int(input("how much would you like to withdraw"))
			currentobject.withdraw(value)
		else:
			print("wrong menu choice")
	elif menu_option==2:
		print("1.deposit funds")
		print("2.withdraw funds")
		submenu_option=int(input())
		if submenu_option==1:
			value=int(input("how much would you like to deposit"))
			currentobject.deposit(value)
		elif submenu_option==2:
			value=int(input("how much would you like to withdraw"))
			currentobject.withdraw(value)
		else:
			print("wrong menu choice")
input()