from CreditCard import CreditCard

class Input:
  # this is going to break down the actual text put in command line/stdin
  def __init__(self, input):
    # using a dictionary to store card numbers is the go to option, using the name as a key
    self.card_book = {}
    # based on the input shown in the example, there can be multiple lines, so we need to separate them
    for line in input:
      # From "Charge Tom $500" to ["Charge", "Tom", "$500"]
      #line = line.strip()
      line = line.split(' ')
      #Based on the 3 input commands, we must do 3 different things
      if line[0] == "Add":
        self.create_account(line)
      if line[0] == "Charge":
        self.charge_account(line)
      if line[0] == "Credit":
        self.credit_account(line);

  # creates the account when command line is "Add"
  def create_account(self, line):
    add, given_name, card_number, limit = line
    # limit is still a "$XXXX" we need to change it to an integer
    limit = int(limit[1:])
    # add a person to the map, where their name is the key and the value it holds is their credit card info
    self.card_book[given_name] = CreditCard(given_name, card_number, limit)

  # charges the account when the command is "Charge"
  def charge_account(self, line):
    action, given_name, charge_amount = line
    charge_amount = int(charge_amount[1:])
    self.card_book[given_name].charge(charge_amount)

  # charges the person's account when the command is "Credit"
  def credit_account(self, line):
      action, given_name, credit_amount = line
      credit_amount = int(credit_amount[1:])
      self.card_book[given_name].credit(credit_amount)

  # displays the current summary of the credit cards within the dictionary
  def summary(self):
    sorted_card_book = dict(sorted((self.card_book.items)(), key=lambda x: x[0].lower()))
    for key in sorted_card_book:
      name = key
      balance = str(sorted_card_book[key].get_balance())
      message = None
      if balance == "error":
        message = "error"
      else:
        message = "$" + str(balance)
      print(name + ": " + message)