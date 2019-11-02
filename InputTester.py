import sys
import unittest
from unittest import TestCase

import sys
from Input import Input
from CreditCard import CreditCard


class tester(TestCase):
    # valid cart luhn10 tests
    def test_valid_ID1(self):
        card_number = "5454545454545454"
        self.card = CreditCard("Kshitij", "5454545454545454", 5000)
        self.assertEqual(self.card.valid_card(card_number), True)

    def test_valid_ID2(self):
        card_number = "1234567890123456"
        self.card = CreditCard("Quincy", "1234567890123456", 8000)
        self.assertEqual(self.card.valid_card(card_number), False)

    def test_valid_ID3(self):
        card_number = "2128529407"
        self.card = CreditCard("Braintree", "2128529407", 9000)
        self.assertEqual(self.card.valid_card(card_number), True)

    # All of these tests test the input class, creating an account, charging, crediting and some edge cases
    def test_single_input(self):
        self.inputter = Input(['Add Lisa 5454545454545454 $3000'])
        self.assertEqual(len(self.inputter.card_book), 1)

    def test_multiple_input(self):
        input_line = ['Add Lisa 5454545454545454 $3000', 'Add Kshitij 79927398713 $6000']
        processor = Input(input_line)
        output = processor.card_book
        self.assertEqual(len(processor.card_book), 2)
    
    #inputting same person, should overwrite, thus keeping the dictionary with 1 key value 
    def test_same_input(self):
        input_line = ['Add Kshitij 79927398713 $6000', 'Add Kshitij 79927398713 $6000']
        processor = Input(input_line)
        output = processor.card_book
        self.assertEqual(len(processor.card_book), 1)
    
    def test_charge_credit_account(self):
        self.inputter = Input(['Add Lisa 5454545454545454 $3000', 'Charge Lisa $8', 'Credit Lisa $100'],)
        value = self.inputter.card_book['Lisa'].get_balance()
        self.assertEqual(value, -92)

    def test_decline_card(self):
        self.decliner = Input(['Add Tom 4111111111111111 $1000', 'Charge Tom $650', 'Charge Tom $800'])
        val = self.decliner.card_book['Tom'].get_balance()
        self.assertEqual(val, 650)

if __name__ == '__main__':
    unittest.main()