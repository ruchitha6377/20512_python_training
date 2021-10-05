import unittest
from loginimport import login


class validtest(unittest.TestCase):
    def test1(self):
        self.assertEqual(login('ruchi', 'ruchitha2'), True)

    def test2(self):
        self.assertEqual(login('ruchitha', 'ruchitha@3'), True)

    def test3(self):
        self.assertEqual(login('ruchiTHA', 'ruchi@1028'), True)

    def test4(self):
        self.assertEqual(login('29-768', 'abc'), False)

    def test5(self):
        self.assertEqual(login(9999, '@#$'), False)

    def test6(self):
        self.assertEqual(login('yathi', 123456), False)

    def setUp(self):
        print("Setup")

    def tearDown(self):
        print("Teardown")

    @classmethod
    def setUpClass(self) \
            -> print("setup class"):
        pass

    @classmethod
    def tearDownClass(self) \
            -> print("teardown"):
        pass




if __name__ == '__main__':
        unittest.main()
