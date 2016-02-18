# -*- coding: UTF-8 -*-

import MySQLdb

connection=MySQLdb.connect(
	host='localhost',
	user='root',
	pass='',
	db='gppex')

cursor = connection.cursor()

cursor.execute('select * from empresa')

for linha in cursor:
	print linha

connection.close()


## CONTINUAR DOS 3 MINUTOS DO VÍDEO 1