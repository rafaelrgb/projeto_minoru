import csv
import socket
import threading
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Worker(threading.Thread):
	# Create an UDP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server_address = ('192.168.4.1', 8888)
	message = 'start'

	should_record = False
	quit = False

	def run(self):
		try:
			while not self.quit:
				if self.should_record:
					print("Iniciando captura de dados...")

					with open('readings.csv', 'w', newline='') as csvfile:
						csv_writer = csv.writer(csvfile)

						# Send data
						sent = self.sock.sendto(self.message.encode('utf-8'), self.server_address)

						# Receive response
						while (self.should_record == True and self.quit == False):
							data, server = self.sock.recvfrom(4096)
							parsedData = parse_data(data.decode('utf-8'))
							csv_writer.writerow(parsedData)

				else:
					time.sleep(0.1)
		finally:
			print ("closing socket")
			self.sock.close()


class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Aquisicao de Dados")
		self.set_border_width(10)

		self.worker = Worker()
		self.worker.start()

		self.box = Gtk.Box(spacing=6)
		self.add(self.box)

		self.start_btn = Gtk.Button(label="Iniciar")
		self.start_btn.connect("clicked", self.on_start_btn_clicked)
		self.box.pack_start(self.start_btn, True, True, 0)

		self.end_btn = Gtk.Button(label="Encerrar")
		self.end_btn.connect("clicked", self.on_end_btn_clicked)
		self.box.pack_start(self.end_btn, True, True, 0)

		self.active = False

	def on_start_btn_clicked(self, widget):
		self.worker.should_record = True
		

	def on_end_btn_clicked(self, widget):
		print("Encerrando captura de dados...")
		self.worker.should_record = False

def parse_data(data):
	return data.split(',')

try:
	win = MainWindow()
	win.connect("destroy", Gtk.main_quit)
	win.show_all()
	Gtk.main()

finally:
	win.worker.quit = True
	win.worker.join()
