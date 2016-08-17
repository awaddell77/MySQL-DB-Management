#mysql 
import re
from soupclass8 import C_sort,r_csv
import csv
print("mysql.connector.connect(user='username', password='passsword', host='127.0.0.1', database='database_name'")
class Db_mngmnt(object):
	def __init__(self, user, password, database):
		self.user = user 
		self.password = password
		self.database = database
	
	def login(self):
		cnx = mysql.connector.connect(user=self.user, password=self.password, host='127.0.0.1', database=self.database)
		cursor = cnx.cursor(buffered = True)
		return cursor

	def import_data(self, fname):
		info = C_sort(fname)
		db_columns = info.row(0)
		db_contents = info.contents[1:]
		return db_columns, db_contents

	def table_create(self, x, table_name, location=''):
		#creates table of text columns usings the provided list as column headers
		new = [re.sub(' ', '_', x[i].strip(' ')) + " TEXT" for i in range(0, len(x))]
		contents = ', '.join(new)
		if location == '':
			return 'CREATE TABLE ' + table_name + ' (' + contents + ') ;'
		else:
			return 'CREATE TABLE ' + table_name +'.'+ location + ' (' + contents + ') ;'
	def table_data_prep(self, x):
		for i in range(0, len(x)):
		#adds quotes to every item on a csv list
			for i_2 in range(0, len(x[i])):
				x[i][i_2] = '"' + x[i][i_2] + '"'
		return x 
	def table_insert(self, x, table):
		results = []
		x = table_data_prep(x)
		for i in range(0, len(x)):
			values = '(' + ', '.join(x[i]) + ') ;'
			command = 'INSERT INTO %s VALUES %s' % (table, values)
		#print(command)
			results.append(command)
		return results
	def row_insert_single(self, table_name, x, database = ''):
		values = ['"' + str(x[i]) + '"' for i in range(0, len(x))]
		if database == '':
			command = "INSERT INTO {0} VALUES ({1})".format(table_name, ", ".join(values))
		else:
			command = "INSERT INTO {0}.{1} VALUES ({2})".format(database, table_name, ", ".join(values))
		return command













test = Db_mngmnt('test','test','test')

