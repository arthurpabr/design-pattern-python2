# -*- coding: UTF-8 -*-

import MySQLdb

class Connection_factory(object):

	def get_connection(self):
		connection=MySQLdb.connect(
			host='localhost',
			user='root',
			passwd='',
			db='gppex')
		return connection