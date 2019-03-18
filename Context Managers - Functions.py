from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
	try:
		f = open(file, mode)
		yield f
	finally:
		f.close()


with open_file('sample_1.txt', 'w') as f:
	f.write('Context Manager - Implemented Using Functions. ')
	
print(f.closed)
