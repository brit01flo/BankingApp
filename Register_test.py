import unittest
from Register.Register import Register 

class TestNewAccount(unittest.TestCase):

    def test_account_random(self):
        """
        Test if the object contains the correct details
        """
        user1NewAccount = Register.generateAccountNo()

        self.assertIsNot(user1NewAccount, "9282729282928290")
        self.assertEqual(user1NewAccount[:2], "89", '')


    def test_create_account(self):
        """
        Test if the object contains the correct details
        """
        user1NewAccount = Register('mphela@gmail.com', 'Tebogo', 'Mphela', '@2Dave@2mano@8')
        print(user1NewAccount.__str__())
        self.assertEqual(user1NewAccount.email, 'mphela@gmail.com', 'checks if the email is correct.')


if __name__ == '__main__':
    unittest.main()
