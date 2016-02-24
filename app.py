# -*- coding: UTF-8 -*-

import MySQLdb
from connection_factory import Connection_factory

connection = Connection_factory().get_connection()
cursor = connection.cursor()
cursor.execute('select * from empresa')
for linha in cursor:
	print linha
connection.close()