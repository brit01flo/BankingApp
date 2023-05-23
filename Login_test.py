import unittest
from Login.Login import Login 
from Common.Common import fethUserInfor, logged_in_user


class TestLogin(unittest.TestCase):

    def test_failed_login(self):
        """
        Test for invalid login details 
        """
        User = Login('mphela@gadil.com', 'asdkfj3nkadjf12$%&%')
        correctDetails = logged_in_user(User.username)

        self.assertEqual(correctDetails, None)


    def test_correct_login(self):
        """
        Test for valid login details
        """
        User = Login("mphela@gmail.com", "@Meno16oneM@")
        correctDetails = logged_in_user(User.username)
        print(correctDetails)

        self.assertEqual(correctDetails[3].strip(), User.username)
        self.assertEqual(correctDetails[4].strip(), User.password)


if __name__ == '__main__':
    unittest.main()
