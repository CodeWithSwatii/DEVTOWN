import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Add the assertion below
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(price, 120.84)  # Ensure the calculated price is correct

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Add the assertion below
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(price, 120.84)  # Ensure the calculated price is correct

    def test_getDataPoint_calculatePriceZeroAsk(self):
        quotes = [
            {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Add the assertion below
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(price, 120.48)  # Ensure the calculated price is correct when ask price is zero

    def test_getDataPoint_calculatePriceZeroBid(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 0}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Add the assertion below
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(price, 119.2)  # Ensure the calculated price is correct when bid price is zero

    # Add more unit tests as needed

if __name__ == '__main__':
    unittest.main()
