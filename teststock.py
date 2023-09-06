# teststock.py

import stock
import unittest

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_create_keyword(self):
        s = stock.Stock(name='GOOG', shares=100, price=490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
    def test_cost(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock('GOOG', 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_from_row(self):
        s = stock.Stock.from_row(['GOOG','100','490.1'])
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

    def test_eq(self):
        a = stock.Stock('GOOG', 100, 490.1)
        b = stock.Stock('GOOG', 100, 490.1)
        self.assertTrue(a==b)

    # Tests for failure conditions
    def test_shares_badtype(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = '50'

    def test_shares_badvalue(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50

    def test_price_badtype(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = '45.23'

    def test_price_badvalue(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -45.23

    def test_bad_attribute(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 100

if __name__ == '__main__':
    unittest.main()


#My code from exercise 5-6 (told to copy from solution to aid moving forward)
'''    # teststock.py

    import unittest
    import stock

    class TestStock(unittest.TestCase):
        def test_create(self):
            s = stock.Stock('GOOG', 100, 490.1)
            self.assertEqual(s.name, 'GOOG')
            self.assertEqual(s.shares, 100)
            self.assertEqual(s.price, 490.1)
        
        def test_keyword_args(self):
            s = stock.Stock(name='GOOG',shares=100,price=490.1)
            self.assertEqual(s.name, 'GOOG')
            self.assertEqual(s.shares, 100)
            self.assertEqual(s.price, 490.1)

        def test_cost(self):
            s = stock.Stock('GOOG', 100, 490.1)
            self.assertEqual(s.cost, 49010.0)
        
        def test_sell(self):
            s = stock.Stock('GOOG', 100, 490.1)
            s.sell(50)
            self.assertEqual(s.shares, 50)

        def test_from_row(self):
            types = (str, int, float)
            record = stock.Stock.from_row(['GOOG',100, 490.1])
            self.assertEqual(stock.Stock.from_row(['GOOG',100, 490.1]), record)


        def test_repr(self):
            s = stock.Stock('GOOG', 100, 490.1)
            self.assertEqual(s.__repr__() ,'Stock(%r, %r, %r)' % (s.name, s.shares, s.price))

        def test_eq(self):
            s = stock.Stock('GOOG', 100, 490.1)
            other = stock.Stock('GOOG', 100, 490.1)
            self.assertEqual(s == other, isinstance(other, stock.Stock) and ((s.name, s.shares, s.price) == (other.name, other.shares, other.price)))


        #Unit Test with Expected Errors
        def test_bad_shares_type(self):
            s = stock.Stock('GOOG', 100, 490.1)
            with self.assertRaises(TypeError):
                s.shares = '50'

        def test_bad_shares_value(self):
            s = stock.Stock('GOOG', 100, 490.1)
            with self.assertRaises(ValueError):
                s.shares = -50
        
        def test_bad_price_type(self):
            s = stock.Stock('GOOG', 100, 490.1)
            with self.assertRaises(TypeError):
                s.price = '490.1'

        def test_bad_price_value(self):
            s = stock.Stock('GOOG', 100, 490.1)
            with self.assertRaises(ValueError):
                s.price = -490.1

        def test_bad_attribute_share(self):
            s = stock.Stock('GOOG', 100, 490.1)
            with self.assertRaises(AttributeError):
                s.share = 50


    if __name__ == '__main__':
        unittest.main()
'''