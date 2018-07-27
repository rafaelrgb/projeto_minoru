import sqlite3

class DatabaseHandler(object):

	def __init__(self, db_name):
		try:
			# conectando...
			self.conn = sqlite3.connect(db_name)
			self.cursor = self.conn.cursor()
			print("Banco:", db_name)
			self.cursor.execute('SELECT SQLITE_VERSION()')
			self.data = self.cursor.fetchone()
			print("SQLite version: %s" % self.data)
		except sqlite3.Error:
			print("Erro ao abrir banco.")
			return False

	def commit_db(self):
		if self.conn:
			self.conn.commit()

	def close_db(self):
		if self.conn:
			self.conn.close()
			print("Conexão fechada.")

	def get_pacient(self, pacientId):
		r = self.cursor.execute('SELECT * FROM pacients WHERE id = ?', (id,))
		return r.fetchone()

	def get_all_pacients(self):

	def save_pacient(self, id, name, birthday, gender, obs):

	def delete_pacient(self, id):

	def get_all_records(self):

	def create_record(self, pacientId, accX, accY, accZ, angX, angY, angZ, temperature, pulse, height):

	def delete_records_from_pacient(self, pacientId):
