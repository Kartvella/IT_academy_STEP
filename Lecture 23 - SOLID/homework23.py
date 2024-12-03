import unittest
from mainlogic import BankAccount, ShoppingCart

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Alice", 100)

    def test_initialization(self):
        self.assertEqual(self.account.owner, "Alice")
        self.assertEqual(self.account.balance, 100)

    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_deposit_negative_amount_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_withdraw_with_sufficient_funds(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    def test_withdraw_exact_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)

    def test_withdraw_with_insufficient_funds_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_initialization(self):
        self.assertTrue(self.cart.is_empty())

    def test_add_item(self):
        self.cart.add_item("Apple", 1.0, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], "Apple")
        self.assertEqual(self.cart.items[0]['price'], 1.0)
        self.assertEqual(self.cart.items[0]['quantity'], 3)

    def test_add_multiple_items(self):
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.add_item("Banana", 0.5, 4)
        self.assertEqual(len(self.cart.items), 2)

    def test_add_item_with_invalid_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", 0.5, 0)

    def test_add_item_with_negative_quantity_raises_error(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("Banana", 0.5, -1)

    def test_total_price(self):
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.add_item("Banana", 0.5, 4)
        self.assertEqual(self.cart.total_price(), 5.0)

    def test_total_price_empty_cart(self):
        self.assertEqual(self.cart.total_price(), 0.0)

    def test_remove_item(self):
        self.cart.add_item("Banana", 0.5, 4)
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], "Banana")

    def test_remove_item_not_in_cart(self):
        self.cart.add_item("Banana", 0.5, 4)
        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)

    def test_is_empty(self):
        self.assertTrue(self.cart.is_empty())
        self.cart.add_item("Apple", 1.0, 3)
        self.assertFalse(self.cart.is_empty())

if __name__ == "__main__":
    unittest.main()