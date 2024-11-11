import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_low_ticket_price(self): #F
        self.assertEqual(self.zoo.get_ticket_price(-1), 'Invalid')

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(65), 100)
    
    def test_boundary1_ticket_price(self): #F
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_boundary2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_boundary3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def test_boundary4_ticket_price(self): #F
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_boundary5_ticket_price(self): #F
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_boundary6_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_boundary7_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
      

        


if __name__ == '__main__':
    unittest.main()