from time import sleep
from datetime import datetime as dt

def profile(FMT):
	def wrapper(func):
		def wrapped(*args, **kwargs):
			start =dt.now()
			res = func(*args, **kwargs)
			end = dt.now()
			print FMT.format(func.__name__, end - start)
			return res

		return wrapped
	return wrapper

@profile('My{} finished in {}')
def slow_func():
	sleep(1)
	return"I'm slow"

print slow_func()