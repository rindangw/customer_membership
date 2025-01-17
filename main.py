from tabulate import tabulate
from math import sqrt


class Membership:

  user_data = {'Sumbul': 'Platinum', 'Ana': 'Gold', 'Cahya': 'Platinum'}


  membership = {
     "Membership":["Platinum", "Gold", "Silver"],
     "Discount":["15%","10%","8%"],
     "Another Benefit":["Benefit Gold + Silver + Cashback max. 30%","Benefit Silver + Voucher Ojek Online", "Voucher Makanan"]
  }

  requirements = {
     "Membership" : ["Platinum", "Gold", "Silver"],
     "Monthly Expense (juta)":[8,6,5], 
     "Monthly Income(juta)":[15,10,7]
  }

  def __init__(self, username):
    self.username = username

  def show_benefit(self):
    print("Benefit Membership PacCommerce\n")
    print(tabulate(self.membership, headers='keys', tablefmt="grid", stralign="center"))

  def show_requirements(self):
    print("Requirements Membership PacCommerce\n")
    print(tabulate(self.requirements, headers='keys', tablefmt="grid", stralign="center", numalign="center"))

  def predict_membership(self, monthly_expense, monthly_income):
    self.monthly_expense = monthly_expense
    self.monthly_income = monthly_income

    euclidean_list = []
    for i in range(len(self.requirements["Membership"])):
      euclidean_user = (sqrt(((monthly_expense - self.requirements["Monthly Expense (juta)"][i])**2)+((monthly_income-self.requirements["Monthly Income(juta)"][i])**2)))
      euclidean_list.append(euclidean_user)

    membership_list = self.requirements["Membership"]
    euclidean_dict = dict(zip(membership_list, euclidean_list))
    print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {euclidean_dict}")
    membership_predict = min(euclidean_dict, key=euclidean_dict.get)
    print(membership_predict)

    if self.username not in self.user_data:
      self.user_data[self.username] = membership_predict


  def show_membership(self):
    if self.username in self.user_data:
      return self.user_data[self.username]

  def calculate_price(self,list_harga_barang):
    self.list_harga_barang = list_harga_barang

    total_harga = sum(list_harga_barang)
    user_membership = self.show_membership()
    index_membership = self.membership["Membership"].index(user_membership)
    discount_str = self.membership["Discount"][index_membership]
    discount = int(discount_str.rstrip("%"))
    final_price = total_harga * (1-(discount/100))
    print(f'Final price: {final_price}')

