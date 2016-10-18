#for normalizing csv files
from soupclass8 import C_sort, r_csv



class Csv_norm(object):
	def __init__(self, fname, datatypes):
		self.fname = fname
		self.dataypes = datatypes
		orig_csv = C_sort(fname)
		contents = self.orig_csv.contents

	def main(self, fname):
		pass

	def int_test(x, repl=1337):
		for i in range(0, len(x)):
			try:
				int(x[i])
			except ValueError as VE:
				x[i] = repl
		return x
	def date_test(x, repl='1337-01-01'):
		for i in range(0, len(x)):
			try:
				x[i].split('-')
			except SyntaxError as SE:
				x[i] = repl
			else:
				if len(x[i].split('-')) != 3 and '/' in x[i]:
					x[i] = re.sub('/', '-', x[i])

		return x






		#examines list and tests for 