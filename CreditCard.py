
class CreditCard:
  # this class is meant to operate only on the values given in the constructor

  # constructor, remember the "add" input constructs a new person
  def __init__(self, given_name, card_number, limit):
    # self is the same "this" as this from C++
    self.given_name = given_name
    # check the card validity after name is set, we still output name and error for balance
    if(self.valid_card(card_number)):
      self.card_number = card_number
      self.limit = limit
      self.account_balance = 0 # must keep track of the balance because of credit and charges
      self.isValid = True

    else:
      self.card_number = "error"
      self.account_balance = "error"
      self.isValid = False


  # validates card based on Luhn 10 algorithm
  def valid_card(self, card_number):
    # converting string word into list of integers
    number_list = list(card_number)
    for i in range(0, len(number_list)): 
      number_list[i] = int(number_list[i]) 
    # double and sum the value of every other digit starting from the rightmost digit
    even_indexes = number_list[-2::-2]
    sum1 = 0
    for i in range(0, len(even_indexes)):
      even_indexes[i] *= 2
      #if the doubled value is greater than 9, then sum the digits of the number (ex: 12 -> 1+2 = 3 same thing as 12 - 9 = 3)
      if even_indexes[i] > 9:
        even_indexes[i] -= 9
      sum1 += even_indexes[i]
    # take the sum of all the odd index values
    odd_indexes = number_list[-1::-2]
    sum2 = 0
    sum2 += sum(odd_indexes)
    # if the total sum modulo 10 equals 0, it's a valid credit card number
    return (((sum1 + sum2) % 10) == 0)

  # to credit the account means to lower the balance (debt) because money is being added
  def credit(self, amount):
    if(self.isValid):
      self.account_balance -= amount

  # to charge the account means to increase the balance (debt) because money is being subtracted
  def charge(self, amount):
    if(not(self.isValid)):
      return
      # if the account is overcharged, pretend as if declined which is why nothing is returned
    if((self.account_balance + amount) <= self.limit):
      self.account_balance += amount
    else:
      return
  
  # we need to return the balance to the output console
  def get_balance(self):
    return self.account_balance;
