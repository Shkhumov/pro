from datetime import datetime as dt

class User(object):
	def __init__(self, name, year):
		self.name = name
		self.year_registered = year

	@property
	def years(self):
	 	return dt.now().year - self.year_registered

class Item(object):
			def __init__(self, name, price):
				self.name = name
				self.price = price
			
			#def _hash__(self):
			#	return'{}:{}'.format(self.name, self.price)

class Order(object):
	def __init__(self, user,item_list):
		self.user = user
		self.items = item_list
	
	@property
	def cost(self):
		return sum([item.price * count for item, count in self.items.items()])

	@property
	def max_single_count(self):
	    return max(self.items.values())

	@property
	def distinct_count(self):
	    return len(self.items.keys())
	
	
if __name__ == '__main__':  #testing   Linox~ python -m unittest discover
	user = User('Ivan', 2002)
	assert user.name == 'Ivan'
	assert user.year_registered == 2002
	assert user.years == 14


	pen = Item('Pen', 1)
	assert pen.name == 'Pen'
	assert pen.price == 1

	order1 = Order(user, {Item('Pensil', 0.5):1, Item('Marker', 1.2):2})
	assert order1.user.name == 'Ivan'
	#assert order1.items[0].name == 'Pensil'
	assert len(order1.items) == 2
	assert order1.cost == 2.9
	assert order1.max_single_count == 2
	order2 = Order(user, {Item('Pensil', 0.5): 10, Item('Marker', 1.2): 10})
	assert order2.max_single_count == 10
	

	#d = {Item('Pensil', 0.5): 10, Item('Marker', 1.2): 5}
	#print d
	print order1.cost