# Basic Credit Card Processing

## Language Style & Design Decision Overview

1. The goal when building this project was to emphasize neat and organized code that is separated into blocks for not only easy reading, but debugging as well. At first, I tried using C++, however I got very confused with syntax dealing with various things such as type casting, reading SDTDIN/command line arguments and using the dictionary/hash map data structure all of which Python and its libraries handled with ease (felt like an early Christmas present). 

As stated, I used the dictionary data structure simply because it was very easy to store the credit card information in which the key was the name of the person and the value was the credit card itself.

2. My implementation of this project was split into three parts:
  - **BTProcessor.py** - This class is quite simple, it handles the two cases of the input.txt file, through STDIN and read from file. Both forms of ./myprogram input.txt' and './myprogram < input.txt are functional. Additionally, this class breaks down the text file into lines and feeds it into the Input class for further processing.
  - **Input.py** - This file takes a broken down input of the text file and processes the right action for the commands detailed within the text, routing the program to add a card, charge/credit someone, or even all three in various ways. It will also display a summary proper summary of the data.
  - **CreditCard.py** - At the lowest level of abstraction, this class builds the Credit Card itself, having checkers for proper card validation, and the ability to adust the account values based on charge and credit actions.
  
3. Additionally, **InputTester.py** tests various cases from validating the Luhn 10 algorithm on some credit card numbers and making sure various Input.py and CreditCard.py functions work properly.
    

## Software Dependencies
 All of my evaluation was done using Python 3 so I recommend running in command line using python3.

## To Run a File:

1. cd path/to/folder/Braintree
2. test_input.txt is a testable file in the Braintree folder
3. To make it simple, putting the file you need to test into the Braintree folder and running the following commands is the easiest route
4. ```./BTProcessor.py filename.txt or ./CCProcessorScript.py < filename.txt``` 


## To Run Tests:

1. cd path/to/folder/Braintree
```
 python3 InputTester.py
```

## Requirements
- The program must accept input from two sources: a filename passed in
  command line arguments and STDIN. For example, on Linux or OSX both
  './myprogram input.txt' and './myprogram < input.txt' should work.
- The program must accept three input commands passed with space delimited
  arguments.
- "Add" will create a new credit card for a given name, card number, and limit
  - Card numbers should be validated using Luhn 10
  - New cards start with a $0 balance
- "Charge" will increase the balance of the card associated with the provided
  name by the amount specified
   - Charges that would raise the balance over the limit are ignored as if they
     were declined
   - Charges against Luhn 10 invalid cards are ignored
- "Credit" will decrease the balance of the card associated with the provided
  name by the amount specified
   - Credits that would drop the balance below $0 will create a negative balance
   - Credits against Luhn 10 invalid cards are ignored
- When all input has been read and processed, a summary should be generated and
  written to STDOUT in the format shown in the example below.
- The summary should include the name of each person followed by a colon and
  balance.
- The names should be displayed alphabetically.
- Display "error" instead of the balance if the credit card number does not pass
  Luhn 10.

## Example Input:

```
Add Tom 4111111111111111 $1000
Add Lisa 5454545454545454 $3000
Add Quincy 1234567890123456 $2000
Charge Tom $500
Charge Tom $800
Charge Lisa $7
Credit Lisa $100
Credit Quincy $200
```

## Example Output:

```
Lisa: $-93
Quincy: error
Tom: $500
```
