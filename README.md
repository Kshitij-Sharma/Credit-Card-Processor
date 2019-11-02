# Basic Credit Card Processing - Kshitij Sharma

## Language Style & Design Decision Overview

1. The goal when building this project was to emphasize neat and organized code that is separated into blocks for not only easy reading, but debugging as well. At first, I tried using C++, however I got very confused with syntax dealing with various things such as type casting, reading SDTDIN/command line arguments and using the dictionary/hash map data structure all of which Python and its libraries handled with ease (felt like an early Christmas present). 

As stated, I used the dictionary data structure simply because it wsa very easy to store the credit card information in which the key was the name of the person and the value was the credit card itself.

2. My implementation of this project was split into three parts:
  - **BTProcessor.py** - This class is quite simple, it handles the two cases of the input.txt file, through STDIN and read from file. Both forms of ./myprogram input.txt' and './myprogram < input.txt are functional. Additionally, this class breaks down the text file into lines and feeds it into the Input class for further processing.
  - **Input.py** - This file takes a broken down input of the text file and processes the right action for the commands detailed within the text, routing the program to add a card, charge/credit someone, or even all three in a row. It will also display a summary proper summary of the data.
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





# BT
