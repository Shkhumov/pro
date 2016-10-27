import unittest
from shop import User, Order, Item 
from shop2 import loyalty_discount, bulk_discount, big_cost_discount

class LoyaltyDiscountTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User('Ivan', 2002)

	def test_positive(self):
		#user = User('Ivan', 2000)
		order = Order(self.user, {Item('Pen', 100): 1})
		self.assertEqual(loyalty_discount(order), 5)
 	
 	def test_zero(self):
		#user = User('Ivan', 2014)
		order = Order(self.user, {Item('Pen', 100): 1})
		self.assertEqual(loyalty_discount(order), 0)

class BulkDiscontTestCase(unittest.TestCase):
	def test_positive(self):
		user = User('Ivan', 2000)
		order = Order(user, {Item('Pen', 1): 200})
		self.assertEqual(loyalty_discount(order), 20)
 	
 	def test_zero(self):
		user = User('Ivan', 2014)
		order = Order(user, {Item('Pen', 200): 1})
		self.assertEqual(loyalty_discount(order), 0)

class BigCostDiscountTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User('Ivan', 2014)

	def test_positive(self):
		#user = User('Ivan', 2014)
		order = Order(self.user, {Item('Pen', 100): 20})
		self.assertEqual(loyalty_discount(order), 80)
 	
 	def test_zero(self):
		#user = User('Ivan', 2014)
		order = Order(self.user, {Item('Pen', 10): 20})
		self.assertEqual(loyalty_discount(order), 0)

class DistictDiscountTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User('Ivan', 2014)

	def test_positive(self):
		order = Order(self.user, {Item('Pen',1): 1,
									Item('Pencil',1): 1,
									Item('Marker',1): 1,
									Item('Notebook',1): 1,
									Item('Book',96): 1})
		self.assertEqual(distinct_discount(order),4)
 	
 	def test_zero(self):
 		self.user.year_registered = 2014
		order = Order(self.user, {Item('Pen', 200): 1})
		self.assertEqual(distinct_discount(order), 0)

class BestDiscountTestCase(unittest.TestCase):

	def setUp(self):
		self.user = User('Ivan', 2014)

	def test_distinct_best(self):
		order = Order(self.user, {Item('Pen',1): 1,
									Item('Pencil',1): 1,
									Item('Marker',1): 1,
									Item('Notebook',1): 1,
									Item('Book',96): 1})
		self.assertEqual(distinct_discount(order))

	def test_loyalty_best(self):
		user = User('Ivan', 2014)
		order = Order(user,{Item('Pen', 100): 1})
		self.assertGreaterEqual(best_discount(order), loyalty_discount(order))

	def test_bulk_best(self):
		order = Order(user,{Item('Pen', 100): 20})
		self.assertGreaterEqual(best_discount(order), big_cost_discount(order))

	def test_best(self):
		order = Order(self.user, {Item('Pen',1): 1,
									Item('Pencil',1): 1,
									Item('Marker',1): 1,
									Item('Notebook',1): 1,
									Item('Book',96): 1})
		self.assertGreaterEqual(distinct_discount(order)
		